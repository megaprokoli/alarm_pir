import RPi.GPIO as GPIO
import constants


class Button:

    def __init__(self, channel):
        self.channel = channel
        self.is_on = False
        self.last_state = 0

        GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def triggered(self):
        input = GPIO.input(self.channel)
        return input == GPIO.LOW

    def switch(self):   # TODO in callback
        self.is_on = not self.is_on
        constants.ACTIVE = self.is_on

        print("System State: ", constants.ACTIVE)
