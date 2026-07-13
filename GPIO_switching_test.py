import time
import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

def select(camera):

    if camera == "A":
        print("Selecting Camera A")

        result = os.system("i2cset -y 10 0x70 0x00 0x04")
        print("i2cset returned:", result)

        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(12, True)

    elif camera == "B":
        print("Selecting Camera B")

        result = os.system("i2cset -y 10 0x70 0x00 0x05")
        print("i2cset returned:", result)

        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(12, True)

    time.sleep(1)

while True:

    select("A")
    time.sleep(3)

    select("B")
    time.sleep(3)
