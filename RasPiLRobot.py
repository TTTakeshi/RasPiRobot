import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

# right arm
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

# left arm
gp_out2 = 21
GPIO.setup(gp_out2, GPIO.OUT)

# motor = GPIO.PWM([channel],[frequency(Hz)])
motor2 = GPIO.PWM(gp_out2, 50)
motor2.start(0.0)

# duty = pulse / cycle
bot2 = 2.5   # -90 = 0.5ms / 20ms = 2.5%
mid2 = 7.25   #   0 = 1.45ms / 20ms = 7.25%
top2 = 12.0  # +90 = 2.4ms / 20ms = 12.0%

motor2.ChangeDutyCycle(bot2)
time.sleep(0.5)

motor2.ChangeDutyCycle(top2)
time.sleep(0.5)

motor2.ChangeDutyCycle(mid2)
time.sleep(0.5)


GPIO.cleanup()