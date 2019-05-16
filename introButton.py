import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT);

while True:
    x = input("1 oder 2: ")
    print(x)
    if x == "1":
        GPIO.output(14, True)
        time.sleep(1.0)
    else:
        GPIO.output(14, False)
        time.sleep(0.5)
            
GPIO.output(14, False)