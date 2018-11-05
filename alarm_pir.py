from hardware.led import Led
import RPi.GPIO as GPIO

if __name__ == "__main__":
    led = Led(23, 15)
    led.test()

    GPIO.cleanup()
    print("done")