import cv2
import os
import sys
import time

sys.path.insert(0, os.path.abspath('..'))
from mlf.core.mk2robot import MK2Robot
from mlf.core.serial_control import SerialControl

class RobotController:

    def __init__(self):
        self.model = MK2Robot()
        self.serial = SerialControl()
        
    def set_position_xyz(self, position):
        """ 
        Set Model position to XYZ absolute coordinates, using MK2Robot inverse kinematics
        param: position must be a list [x, y, z], where x, y and z are absolute distance values in mm
        """
        [x, y, z] = position
        self.model.inverse_kinematics(x, y, z)
        q = self.model.q
        s = self.model.servo_equivalent_angles(q)
        self.serial.write_servo(0, s[0])
        self.serial.write_servo(1, s[1])
        self.serial.write_servo(2, s[2])

    def move_belt(self,direction):
        if direction == "F":
            self.serial.write_servo(7,1)
        elif direction == "B":
            self.serial.write_servo(7,0)

    def turn_servo_eff(self,ang):
        self.serial.write_servo(4,ang)
   
    def electro_status(self,status):
        self.serial.write_servo(5,status)

