import serial


class Serial_control:
    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port

    def run_serial(self):
        ser = serial
        try:
            ser = serial.Serial(self.port, 115200, timeout=1)
            print("The port is available")

        except serial.serialutil.SerialException:
            print("The port is at use")
            ser.close()
            ser.open()
