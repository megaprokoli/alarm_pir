import RPi.GPIO as GPIO


class PirSensor:

    def __init__(self, channel):
        self.channel = channel

        GPIO.setup(self.channel, GPIO.IN)

    def triggered(self):
        input = GPIO.input(self.channel)
        return input == GPIO.HIGH

