from threading import Thread
import time


class EventListener(Thread):

    def __init__(self, event, callback):
        super().__init__()

        self.alive = False

        self.event = event
        self.callback = callback

    def run(self):
        if self.callback is None or self.event is None:
            return

        self.alive = True

        while self.alive:
            if self.event():
                if isinstance(self.callback, list):
                    for call in self.callback:
                        call()
                else:
                    self.callback()

                time.sleep(0.5)    # debounce

    def kill(self):
        self.alive = False
