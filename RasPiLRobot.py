import RPi.GPIO as GPIO
import time
import threading
import pygame.mixer

GPIO.setmode(GPIO.BCM) 
pygame.mixer.init()

MAX_LOOP_NUM = 10

# duty = pulse / cycle
bot = 2.5   # -90 = 0.5ms / 20ms = 2.5%
mid = 7.25   #   0 = 1.45ms / 20ms = 7.25%
top = 12.0  # +90 = 2.4ms / 20ms = 12.0%

bot2 = 2.5   # -90 = 0.5ms / 20ms = 2.5%
mid2 = 7.25   #   0 = 1.45ms / 20ms = 7.25%
top2 = 12.0  # +90 = 2.4ms / 20ms = 12.0%

pygame.mixer.music.load('WALLE 4.mp3')
pygame.mixer.music.play()
time.sleep(3)

class MyThread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "MyThread1"
    def run(self):
        # right arm
        gp_out = 3
        GPIO.setup(gp_out, GPIO.OUT)

        motor = GPIO.PWM(gp_out, 50)
        motor.start(0.0)

        motor.ChangeDutyCycle(bot)
        time.sleep(0.5)

        motor.ChangeDutyCycle(top)
        time.sleep(0.5)

        motor.ChangeDutyCycle(mid)
        time.sleep(0.5)

        for iLoop in range(MAX_LOOP_NUM):

            soundR2D2yeah = pygame.mixer.Sound("R2D2-do.wav")
            soundR2D2yeah.play()

            motor.ChangeDutyCycle(bot)
            time.sleep(0.5)

            motor.ChangeDutyCycle(mid)
            time.sleep(0.5)

class MyThread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "MyThread2"
    def run(self):
        # left arm
        gp_out2 = 21
        GPIO.setup(gp_out2, GPIO.OUT)

        # motor = GPIO.PWM([channel],[frequency(Hz)])
        motor2 = GPIO.PWM(gp_out2, 50)
        motor2.start(0.0)

        motor2.ChangeDutyCycle(top2)
        time.sleep(0.5)

        motor2.ChangeDutyCycle(bot2)
        time.sleep(0.5)

        motor2.ChangeDutyCycle(mid2)
        time.sleep(0.5)

        for iLoop2 in range(MAX_LOOP_NUM/2):

            soundR2D2few = pygame.mixer.Sound("R2D2-yeah.wav")
            soundR2D2few.play()

            time.sleep(1.0)
            motor2.ChangeDutyCycle(top2)
            time.sleep(0.5)

            motor2.ChangeDutyCycle(mid2)
            time.sleep(0.5)

thread1 = MyThread1()
thread2 = MyThread2()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

GPIO.cleanup()