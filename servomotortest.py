import RPi.GPIO as GPIO
from time import sleep

# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)
# Zet waarschuwingen uit.
GPIO.setwarnings(False)

# Zet de GPIO pin als uitgang.
GPIO.setup(4, GPIO.OUT)
# Configureer de pin voor PWM met een frequentie van 50Hz.
p = GPIO.PWM(4, 50)
# Start PWM op de GPIO pin met een duty-cycle van 6%
p.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(4, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(4, False)
    p.ChangeDutyCycle(0)

# SetAngle(0)

def passwd(wat):
    if wat == 'abc':
        print('juist passwd')
        SetAngle(180)
        sleep(8)
        SetAngle(0)

while True:
    passwd(input('enter'))


p.stop()
GPIO.cleanup()
