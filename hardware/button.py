import RPi.GPIO as GPIO
from events.event_listener import EventListener


class Button:

    def __init__(self, port, callback_off, callback_on):
        self.port = port
        self.on_event = EventListener(event=self.is_on(), callback=callback_on)

    def is_on(self):
        return GPIO.input(self.port) == GPIO.HIGH
