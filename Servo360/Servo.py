import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

pwm=GPIO.PWM(11,50)

pwm.start(7.5)

pwm.ChangeDutyCycle(6.4)
time.sleep(1)
pwm.ChangeDutyCycle(7)
time.sleep(1)
pwm.ChangeDutyCycle(7.2)
time.sleep(1)
pwm.ChangeDutyCycle(7.2)
time.sleep(1)
pwm.ChangeDutyCycle(7.6)
time.sleep(1)
pwm.ChangeDutyCycle(8)
time.sleep(1)
pwm.ChangeDutyCycle(8.5)
time.sleep(1)
pwm.ChangeDutyCycle(7.2)


GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)

pwm=GPIO.PWM(13,50)

pwm.start(7.5)

pwm.ChangeDutyCycle(8.5)
time.sleep(1)
pwm.ChangeDutyCycle(8)
time.sleep(1)
pwm.ChangeDutyCycle(7.6)
time.sleep(1)
pwm.ChangeDutyCycle(7.23)
time.sleep(1)
pwm.ChangeDutyCycle(7.23)
time.sleep(1)
pwm.ChangeDutyCycle(7)
time.sleep(1)
pwm.ChangeDutyCycle(6.4)
time.sleep(1)
pwm.ChangeDutyCycle(7.23)




