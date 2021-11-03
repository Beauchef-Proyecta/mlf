import sys
sys.path.append('/home/pi/mlf/core')
from serial_control import Serial_control
#from core.serial_control import Serial_control #for pc
import time

robot_serial = Serial_control()
robot_serial.run_serial()
for i in range(10):
    robot_serial.write_servo(3, -4 * i + 90)
    robot_serial.write_servo(2, 4 * i + 90)
    robot_serial.write_servo(1, 10 * i)
    time.sleep(1.2)
robot_serial.read_status()
robot_serial.read_sensors()
robot_serial.run_effector()

robot_serial.close_Serial()
