import time

from serial import Serial
from serial.serialutil import SerialException

class SerialController:
    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = None

    def open(self):
        try:
            self.serial = Serial(self.port, 115200)
            print("The port is available")
        except SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close(self):
        self.serial.close()

    def send_data(self, data):
        self.serial.write(data)
        time.sleep(0.01)
        return self.serial.read(2)

    def build_serial_msg(self, cmd: int, params: list):
        data = [HEADER, len(params) + 1, cmd]
        for p in params:
            data.append(p)
        return bytearray(data)
