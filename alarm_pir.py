from hardware.led import Led
from hardware.button import Button
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    led = Led(23, 15)
    butt = Button(25, callback_on=led.test)

    GPIO.cleanup()
    print("done")
