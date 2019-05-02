# import statements
import random
import time
import RPi.GPIO as GPIO
# initialize global variable for decision point
global dp
dp = 127
# Setup GPIO pins
# Set the BCM mode
GPIO.setmode(GPIO.BCM)
# Outputs
GPIO.setup( 4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
# Input
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# Setup the callback function
def changeDecisionPt(channel):
    global dp
    dp = dp + 1
    if dp == 255: # do not increase dp beyond 255
        dp =255
# Add event detection and callback assignment
GPIO.add_event_detect(27, GPIO.RISING, callback=changeDecisionPt)
while True:
    rn = random.randint(0,255)
    print(dp)
    # useful to check on the dp value print 'dp = ', dp
    if rn <= dp:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(4, GPIO.LOW)
    else:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(17, GPIO.LOW)

