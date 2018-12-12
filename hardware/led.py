import RPi.GPIO as GPIO
import time


class Led:

    def __init__(self, green_port, red_port):
        self.gport = green_port
        self.rport = red_port

        GPIO.setup(self.gport, GPIO.OUT)
        GPIO.setup(self.rport, GPIO.OUT)

    def turn_red(self, t=0):
        GPIO.output(self.gport, GPIO.LOW)
        GPIO.output(self.rport, GPIO.HIGH)

        if t != 0:
            time.sleep(t)
            self.turn_off()

    def turn_green(self, t=0):
        GPIO.output(self.rport, GPIO.LOW)
        GPIO.output(self.gport, GPIO.HIGH)

        if t != 0:
            time.sleep(t)
            self.turn_off()

    def turn_off(self):
        GPIO.output(self.rport, GPIO.LOW)
        GPIO.output(self.gport, GPIO.LOW)

    def test(self):
        print("testing LED...")

        self.turn_red(2)
        self.turn_green(2)
