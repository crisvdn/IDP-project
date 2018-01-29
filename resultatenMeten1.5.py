import signal
import RPi.GPIO as GPIO
import time

import sys
from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

GPIO.setmode(GPIO.BOARD)
#Hier worden de BCM pin's aan de variabelen toegewezen.
rotaryEncoderRechts = 35
rotaryEncoderLinks = 37
rotaryEncoderDruk = 5
knopGeel = 33
knopRood = 3
#Hier worden de BCM pin's in een tuple gezet voor de segmenten van de getallen.
segments = (29, 7, 16, 38, 40, 31, 12, 32)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

#Hier worden de BCM pin's in een tuple gezet voor de getallen.
digits = (15, 13, 11, 36)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

#Hier wordt toegewezen voor welk nummer, welk segment aan of uit moet.

num = {' ': (0, 0, 0, 0, 0, 0, 0),
       '0': (1, 1, 1, 1, 1, 1, 0),
       '1': (0, 1, 1, 0, 0, 0, 0),
       '2': (1, 1, 0, 1, 1, 0, 1),
       '3': (1, 1, 1, 1, 0, 0, 1),
       '4': (0, 1, 1, 0, 0, 1, 1),
       '5': (1, 0, 1, 1, 0, 1, 1),
       '6': (1, 0, 1, 1, 1, 1, 1),
       '7': (1, 1, 1, 0, 0, 0, 0),
       '8': (1, 1, 1, 1, 1, 1, 1),
       '9': (1, 1, 1, 1, 0, 1, 1)}

#Hier wordt de setup aangewezen voor de knopjes.
GPIO.setup(rotaryEncoderRechts, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotaryEncoderLinks, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(knopGeel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotaryEncoderDruk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(knopRood, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print ("scan uw pasje om uw gegevens op te slaan.")
clkLastState = GPIO.input(rotaryEncoderRechts)
teller = 0
gewicht = 0
uniqueID = ""
readOut = 0
try:
    while readOut == 0:
        if GPIO.input(knopGeel) == False:
            readOut = 1
            time.sleep(0.1)
        n = time.ctime()[11:13] + time.ctime()[14:16]
        s = str(n).rjust(4)
        for digit in range(4):
            for loop in range(0, 7):
                GPIO.output(segments[loop], num[s[digit]][loop])
                if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                    GPIO.output(32, 1)
                else:
                    GPIO.output(32, 0)
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)
        while readOut == 1:
            if readOut == 0:
                break
            rdr.wait_for_tag()
            (error, data) = rdr.request()
            (error, uid) = rdr.anticoll()
            print("Hallo *Klant*")
            if not error:
                for i in range(len(uid)-1):
                    uniqueID += str(uid[i])
                    print (uniqueID)
            while len(uniqueID)>9:
                if readOut == 0:
                    break
                print("Oefening is gestart.")
                teller += 0
                readOut = 2
                while readOut == 2:
                        clkState = GPIO.input(rotaryEncoderRechts)
                        dtState = GPIO.input(rotaryEncoderLinks)
                        if clkState != clkLastState:
                                if dtState != clkState:
                                        gewicht+= 1
                                else:
                                        gewicht -= 1
                                        if int(gewicht) < 0:
                                            gewicht = 0
                                print gewicht
                        if GPIO.input(knopGeel) == False:
                            print("Gele knop is ingedrukt. U bent gestopt")
                            readOut = 0
                            print (readOut)
                            time.sleep(0.3)
                        g = str(gewicht).rjust(4)
                        for digit in range(4):
                            for loop in range(0, 7):
                                GPIO.output(segments[loop], num[g[digit]][loop])
                                if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                                    GPIO.output(32, 1)
                                else:
                                    GPIO.output(32, 0)
                            GPIO.output(digits[digit], 0)
                            time.sleep(0.001)
                            GPIO.output(digits[digit], 1)
                        clkLastState = clkState
                        if GPIO.input(rotaryEncoderDruk) == False:
                            readOut = 3
                            print("Draaiknop is ingedrukt. U kunt nu sporten")
                            time.sleep(0.3)
                            while readOut == 3:
                                if GPIO.input(knopRood) == False:
                                    print("Rode knop is ingedrukt. 1 Herhaling toegevoegd")
                                    teller += 1
                                    time.sleep(0.3)
                                if GPIO.input(knopGeel) == False:
                                    print("Gele knop ingedrukt. Herhalingen opgeslagen")
                                    #Hier moet het gewicht + de Herhalingen worden opgestuurd naar de database.
                                    time.sleep(0.2)
                                    teller = 0
                                    time.sleep(0.3)
                                    readOut = 2
                                s = str(teller).rjust(4)
                                for digit in range(4):
                                    for loop in range(0, 7):
                                        GPIO.output(segments[loop], num[s[digit]][loop])
                                        if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                                            GPIO.output(32, 1)
                                        else:
                                            GPIO.output(32, 0)
                                    GPIO.output(digits[digit], 0)
                                    time.sleep(0.001)
                                    GPIO.output(digits[digit], 1)
                                if readOut == 2:
                                    break
                            if readOut == 1:
                                break
                        if readOut == 0:
                            break

finally:
    GPIO.cleanup()
