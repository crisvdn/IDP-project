#!/usr/bin/python
import psycopg2
import signal
import time
import sys
from pirc522 import RFID
import RPi.GPIO as GPIO
from time import sleep
import smbus

GPIO.setwarnings(False)


#scherm
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

LCD_BACKLIGHT  = 0x08  # On 0X08 / Off 0x00

ENABLE = 0b00000100 # Enable bit

E_PULSE = 0.0005
E_DELAY = 0.0005

bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def main():

  lcd_init()

  lcd_string("Houd uw kaart",LCD_LINE_1)
  lcd_string( '    >>>0<<<     ' ,LCD_LINE_2)

def hello():
    lcd_init()
    naam_klant = klant[1]
    naampie = naam_klant.capitalize()
    lcd_string('Hello '+ naampie ,LCD_LINE_1)

def gedag():
    lcd_init()
    naam_klant = klant[1]
    naampie = naam_klant.capitalize()
    lcd_string('   Tot ziens ',LCD_LINE_1)
    lcd_string( '   '+ naampie ,LCD_LINE_2)


def aantal_klanten():
    lcd_init()
    aantal = len(klant_lijst)
    if aantal == 0:
        lcd_string("U bent de eerste",LCD_LINE_1)
        lcd_string( "sporter aanwezig" ,LCD_LINE_2)
    elif aantal == 1:
        lcd_string("Er is momenteel",LCD_LINE_1)
        lcd_string( str(len(klant_lijst)) + ' sporter' ,LCD_LINE_2)
    else:
        lcd_string("Er zijn momenteel",LCD_LINE_1)
        lcd_string( str(len(klant_lijst)) + ' sporters' ,LCD_LINE_2)



def none_lcd():

  lcd_init()
  lcd_string('Kaart Ongeldig' ,LCD_LINE_1)






#psycopg2
conn = psycopg2.connect('host=192.168.42.1 user=hysen password=2140321maya dbname=sportschool')
cur = conn.cursor()
#RFID Variablen
run = True
rdr = RFID()
util = rdr.util()
util.debug = True
# poortje
GPIO.setmode(GPIO.BOARD)
motor = 32
GPIO.setup(motor, GPIO.OUT)
pwm=GPIO.PWM(motor, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle /18 + 2
    GPIO.output(motor, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(motor, False)
    pwm.ChangeDutyCycle(0)

def in_open():
    SetAngle(0)
    aantal_klanten()
    sleep(5)
    SetAngle(90)
def out_open():
    SetAngle(180)
    sleep(5)
    SetAngle(90)

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()
    #pmw.stop()
    #lcd_byte(0x01, LCD_CMD)
    #cur.close()
    #conn.close()


signal.signal(signal.SIGINT, end_read)
print("scan uw pasje << Database")
main()


def get_all_personen():
    query = """
    SELECT
        klant_id, voornaam
    FROM
        klant
    """
    cur.execute(query)
    return cur.fetchall()
klant_lijst = []
klantIngeschreven = 0
while run:
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    (error, uid) = rdr.anticoll()
    if not error:
        Unique_id = ''
        for i in uid:
            Unique_id+= str(i)
        klanten = get_all_personen()
        for klant in klanten:
            if klant[0] == Unique_id:
                klantIngeschreven = 1
        if klantIngeschreven == 0:
            none_lcd()
            time.sleep(5)
            main()
        if klantIngeschreven == 1:
            for klant in klanten:
                if klant[0] == Unique_id and klant[0] in klant_lijst:
                    gedag()
                    out_open()
                    klant_lijst.remove(klant[0])
                    main()
                elif klant[0] == Unique_id and klant[0] not in klant_lijst:
                    hello()
                    in_open()
                    klant_lijst.append(klant[0])
                    main()
            klantIngeschreven = 0
