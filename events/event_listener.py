from threading import Thread


class EventListener(Thread):

    def __init__(self, event, callback):
        super().__init__()

        self.event = event
        self.callback = callback

    def run(self):
        if self.callback is None or self.event is None:
            return

        while True:
            if self.event():
                self.callback()
