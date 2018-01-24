import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#Hier worden de BCM pin's aan de variabelen toegewezen.
knop1 = 19
knop2 = 26

#Hier worden de BCM pin's in een tuple gezet voor de segmenten van de getallen.
segments = (5, 4, 23, 20, 21, 6, 18, 12)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

#Hier worden de BCM pin's in een tuple gezet voor de getallen.
digits = (22, 27, 17, 16)

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

#Hier wordt de setup aangewezen voor knop 1 en knop 2.
GPIO.setup(knop1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(knop2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print ("Druk op knop 1 om te tellen, knop 2 om af te sluiten.")
teller = 0
knopStaat = False
try:
    while True:
        if GPIO.input(knop1) == True:
            print("Oefening is gestart.")
            teller += 0
            knopStaat = True
            while knopStaat == True:
                if GPIO.input(knop1) == True:
                    print("knop 1 is ingedrukt.")
                    teller += 1
                    knopStaat = True
                    time.sleep(0.2)
                s = str(teller).rjust(4)
                for digit in range(4):
                    for loop in range(0, 7):
                        GPIO.output(segments[loop], num[s[digit]][loop])
                        if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                            GPIO.output(12, 1)
                        else:
                            GPIO.output(12, 0)
                    GPIO.output(digits[digit], 0)
                    time.sleep(0.001)
                    GPIO.output(digits[digit], 1)
                if GPIO.input(knop2) == True:
                    print("knop 2 is ingedrukt, teller is gereset en gegevens zijn opgeslagen.")
                    teller = 0
                    time.sleep(0.2)
finally:
    GPIO.cleanup()
