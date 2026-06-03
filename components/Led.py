import RPi.GPIO as GPIO

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print(f"LED initialized on pin {pin}")
    
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
    
    def toggle(self):
        GPIO.output(self.pin, not GPIO.input(self.pin))

    def get_state(self):
        return "on" if GPIO.input(self.pin) else "off"

    def cleanup(self):
        self.off()