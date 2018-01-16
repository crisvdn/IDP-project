import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
motor = 3
knop = 11
GPIO.setup(motor, GPIO.OUT)
GPIO.setup(knop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm=GPIO.PWM(motor, 50)

pwm.start(0)

def setAngle(angle):
    duty = angle /18 + 2
    GPIO.output(motor, True)
    pwm.ChangeDutyCycle(duty)
    GPIO.output(motor, False)
    pwm.ChangeDutyCycle(0)

while True:
    input_state = GPIO.input(knop)
    if input_state == False:
        setAngle(45)
        print('Poort geopend')
        sleep(3)
        setAngle(140)
