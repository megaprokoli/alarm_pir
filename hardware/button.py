import RPi.GPIO as GPIO
from events.event_listener import EventListener


class Button:

    def __init__(self, port, callback_off=None, callback_on=None):
        self.port = port
        self.on_event = EventListener(event=self.is_on(), callback=callback_on)
        self.off_event = EventListener(event=self.is_off(), callback=callback_off)

    def is_on(self):
        return GPIO.input(self.port) == GPIO.HIGH

    def is_off(self):
        return not self.is_on()
