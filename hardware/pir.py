class PirSensor:

    def __init__(self, out_port, callback_triggered):
        self.out_port = out_port
        self.triggered = callback_triggered
