
import serial
from serial import Serial
import time

class SerialControl:

    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = None

    def open_serial(self):
        try:
            self.serial = Serial(self.port, 115200, timeout=0.1, write_timeout=0.1)
            print("The port is available")
            serial_port = "Open"
            time.sleep(2)
        except serial.serialutil.SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close_serial(self):
        self.serial.close()

    def send_data(self, data):
        self.serial.write(data)
        return self.serial.readline()


if __name__ == "__main__":
    ser = SerialControl("/dev/tty.wchusbserial14140")
    ser.open_serial()
    i=0
    while True:
        i += 1
        i %= 180

        data = bytearray([0x10, i, 0xFE])
        s = ser.send_data(data)
        # print(f"{i}: {s}")

    