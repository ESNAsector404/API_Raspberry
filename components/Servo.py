import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.angle = 0

        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)

    def angle_to_duty_cycle(self, angle):
        return 2.5 + angle / 18

    def set_angle(self, angle):
        self.angle = angle

        duty = self.angle_to_duty_cycle(angle)

        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)  # laisser le temps au servo de bouger
        self.pwm.ChangeDutyCycle(0)

    def get_angle(self):
        return self.angle

    def cleanup(self):
        self.pwm.stop()