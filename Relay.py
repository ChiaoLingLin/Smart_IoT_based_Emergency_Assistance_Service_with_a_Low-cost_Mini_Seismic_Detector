import RPi.GPIO as GPIO

class Relay:
    def __init__(self, gpio:int=23):
        self.gpio = gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.OUT)
        GPIO.output(self.gpio,0)

    def turn_on(self):
        GPIO.output(self.gpio,0)
        #注意是否為低電平觸發

    def turn_off(self):
        GPIO.output(self.gpio,1)    

    def __del__(self):
        GPIO.cleanup()