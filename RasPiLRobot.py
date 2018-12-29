import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
# GPIO.setup(2,GPIO.OUT)
# for iLoop in range(5):
#    GPIO.output(2,True)   
#    time.sleep(1)
#    GPIO.output(2,False)   
#    time.sleep(1)

gp_out = 3
GPIO.setup(gp_out, GPIO.OUT)

# motor = GPIO.PWM([channel],[frequency(Hz)])
motor = GPIO.PWM(gp_out, 50)
motor.start(0.0)

# duty = pulse / cycle
bot = 2.5   # -90 = 0.5ms / 20ms = 2.5%
mid = 7.25   #   0 = 1.45ms / 20ms = 7.25%
top = 12.0  # +90 = 2.4ms / 20ms = 12.0%

motor.ChangeDutyCycle(bot)
time.sleep(0.5)

motor.ChangeDutyCycle(top)
time.sleep(0.5)

motor.ChangeDutyCycle(mid)
time.sleep(0.5)

GPIO.cleanup()