import RPi.GPIO as GPIO

in_ch = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(in_ch, GPIO.IN)

while True:
    if GPIO.input(in_ch):
        print("|", end='')
    else:
        print(".", end='')
