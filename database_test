import psycopg2
import signal
import time
import sys
from pirc522 import RFID
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
conn = psycopg2.connect('host=hysen user=hysen password=2140321maya dbname=test')
cur = conn.cursor()

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)
print("scan uw pasje >> Database")

def add_person(p_id, naam, gewicht):
    query = """
    INSERT INTO
        persoon
    VALUES
        (%s, %s, %s)
    """
    values = (p_id, naam, gewicht)
    cur.execute(query, values)
    conn.commit()


def get_all_persons():
    query = """
    SELECT
        *
    FROM
        persoon
    """
    cur.execute(query)
    return cur.fetchall()

while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    #if not error:
        #print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        k_id = ''
        #print(uid)
        for i in uid:
            k_id+= str(i)
        break

print(k_id)
add_person(k_id , input('naam: '), eval(input('gewicht(kg): ')))





cur.close()
conn.close()
