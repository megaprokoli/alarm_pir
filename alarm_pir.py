from hardware.led import Led
from hardware.button import Button
from hardware.pir import PirSensor
from network.mailer import Mailer
from constants import config
from functools import partial
from events.event_listener import EventListener
import RPi.GPIO as GPIO
import constants
import argparse


def trigger_alarm():
    global mailer

    if constants.ACTIVE:
        constants.TRIGGERED = True
        try:
            mailer.send_msg("alarm und so")
        except Exception as ex:                 # TODO if error mailer reconnect
            print("Failed to send mail: " + str(ex))


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pir", help="use pir motion sensor", action="store_true")
    args = parser.parse_args()

    mailer = Mailer(
        config.get("DEFAULT", "sendMail"),
        config.get("DEFAULT", "receiveMail"),
        config.get("DEFAULT", "password"),
        (config.get("DEFAULT", "smtp"), int(config.get("DEFAULT", "port")))
    )

    if args.pir:
        led = Led(15, 23)
        butt = Button(25)
        pir = PirSensor(14)

        ev_listener_button = EventListener(event=butt.triggered, callback=butt.switch)
        ev_listener_pir = EventListener(event=pir.triggered, callback=trigger_alarm)

        constants.ACTIVE_EV += [ev_listener_button, ev_listener_pir]

        ev_listener_button.start()
        ev_listener_pir.start()

        # GPIO Test
        led.test()
        print("PIR mode")

    else:
        led = Led(15, 23)
        butt = Button(25)

        constants.ACTIVE = True

        ev_listener_button = EventListener(event=butt.triggered, callback=[trigger_alarm, partial(led.turn_red, 120),
                                                                           led.turn_green])

        constants.ACTIVE_EV.append(ev_listener_button)

        ev_listener_button.start()

        # GPIO Test
        led.test()
        led.turn_green()

        print("button mode")

    try:
        [th.join() for th in constants.ACTIVE_EV]
    except KeyboardInterrupt:
        [th.kill() for th in constants.ACTIVE_EV]
        print("canceled")
    finally:
        GPIO.cleanup()

    print("main thread done")
