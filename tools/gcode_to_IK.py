import re
import time
import numpy as np
import sys
sys.path.append('/home/pi/mlf/core')
from serial_control import SerialControl
from mk2robot import MK2Robot
#from core.serial_control import SerialControl #for pc
#from core.mk2robot import MK2Robot #for pc

import argparse

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot_serial = SerialControl()
robot_serial.open_serial()

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()


def goal(array):
    arr = array
    x_sol = arr[0, :]
    y_sol = arr[1, :]
    z_sol = arr[2, :]
    for i in range(len(arr[0, :])):
        q0, q1, q2 = robot.inverse_kinematics(x_sol[i], y_sol[i], z_sol[i])
        robot_serial.write_servo(1, 45 + q0)
        robot_serial.write_servo(2, 90 - q1)
        robot_serial.write_servo(3, q1 + q2)
        time.sleep(0.4)


with open(args.filename) as gcode:
    X_list = np.array([])
    Y_list = np.array([])
    Z_list = np.array([])
    for line in gcode:
        line = line.strip()
        coord = re.findall(r'[XY].?\d+.\d+', line)
        coord_Z = re.findall(r'[YZ].?\d+.\d+', line)
        if coord:
            X_list = np.append(X_list, float(coord[0][1:]))
            Y_list = np.append(Y_list, float(coord[1][1:]))
        if coord_Z:
            Z_list = np.append(Z_list, float(coord_Z[1][1:]))

    goal_XYZ = np.array([X_list, Y_list, Z_list])
    goal(goal_XYZ)

robot_serial.read_status()
robot_serial.read_sensors()
robot_serial.run_effector()

robot_serial.close_serial()