import RPi.GPIO as GPIO
import time


class Led:

    def __init__(self, green_port, red_port):
        self.gport = green_port
        self.rport = red_port

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gport, GPIO.OUT)
        GPIO.setup(self.rport, GPIO.OUT)

    def turn_red(self):
        GPIO.output(self.gport, GPIO.LOW)
        GPIO.output(self.rport, GPIO.HIGH)

    def turn_green(self):
        GPIO.output(self.rport, GPIO.LOW)
        GPIO.output(self.gport, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.rport, GPIO.LOW)
        GPIO.output(self.gport, GPIO.LOW)

    def test(self):
        self.turn_red()
        time.sleep(2)
        self.turn_green()
        time.sleep(2)
        self.turn_off()
