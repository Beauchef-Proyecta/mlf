from serial import Serial
import time

class Serial_control:

    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = Serial

    def run_serial(self):
        try:
            self.serial = Serial(self.port, 115200, timeout=1)
            print("The port is available")
            serial_port = "Open"
        except serial.serialutil.SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close_Serial(self):
        self.serial.close()

    def write_servo(self, id, ang):
        angleData = ang
        if id == 1:
            angleData = 2 * angleData
        self.serial.write(('&' + str(id) + ':'+ str(angleData)).encode())
        time.sleep(0.5)
        print("listo")

    def read_status(self):
        status = "clean"
        print(f"status: {status}")

    def read_sensors(self):
        status = "clean"
        print(f"Sensor status: {status}")

    def run_effector(self):
        status = "ON"
        print(f"Effector status: {status}")
