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
knop1 = 35
knop2 = 37
knop3 = 33
knop4 = 5
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
#Knop 1 is S1
#Knop 2 is S2
#Knop 3 is het gele knopje
#Knop 4 is het rode knope.
GPIO.setup(knop1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(knop2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(knop3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(knop4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print ("scan uw pasje om uw gegevens op te slaan.")
teller = 0
gewicht = 0
uniqueID = ""
readOut = 0
try:
    while readOut == 0:
        rdr.wait_for_tag()
        (error, data) = rdr.request()
        (error, uid) = rdr.anticoll()
        print("Hallo *Klant*")
        if not error:
            for i in range(len(uid)-1):
                uniqueID += str(uid[i])
        while len(uniqueID)>9:
            if GPIO.input(knop1) == True:
                print("Oefening is gestart.")
                teller += 0
                readOut = 1
                while readOut == 1:
                    # Deze eerste if-statement kan veranderd worden naar iets makkelijkers om
                    # het programma te stoppen.
                    if GPIO.input(knop1) == True and GPIO.input(knop2) == True:
                        print ("U bent gestopt")
                        readOut = 0
                        uniqueID = ""
                        teller = 0
                        gewicht = 0
                        time.sleep(0.3)
                        break
                    if GPIO.input(knop1) == True:
                        print("knop 1 is ingedrukt. 10kg toegevoegd.")
                        gewicht += 10
                        time.sleep(0.3)
                    if GPIO.input(knop2) == True:
                        print("knop 2 is ingedrukt. 1kg toegeovegd.")
                        gewicht += 1
                        time.sleep(0.3)
                    if GPIO.input(knop3) == False:
                        print("Knop 3 is ingedrukt. Gewicht gereset.")
                        gewicht = 0
                        time.sleep(0.3)
                    if GPIO.input(knop4) == False:
                        readOut = 2
                        print("Knop 4 is ingedrukt. U kunt nu sporten")
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
                        while readOut == 2:
                            if GPIO.input(knop1) == True:
                                print("knop 1 is ingedrukt. 1 Herhaling toegevoegd")
                                teller += 1
                                time.sleep(0.3)
                            if GPIO.input(knop2) == True:
                                print("knop 2 is ingedrukt. Herhalingen opgeslagen")
                                teller = 0
                                time.sleep(0.3)
                                readOut = 1
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
                            if readOut == 1:
                                break

finally:
    GPIO.cleanup()
