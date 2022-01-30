from .serial_control import SerialController


class MK2Serial:
    
    HEADER = 0xA0
    CMD_JOINT = 0x10
    CMD_BELT = 0x20
    CMD_GRIPPER = 0x30
    CMD_MAGNET = 0x40
    CMD_PROXIMITY = 0xA0
    CMD_LASER = 0xB0
    
    def __init__(self):
        self.serial = SerialController()
    
    def set_joints(self, angles: list):
        data = self.serial.build_serial_msg(self.CMD_JOINT, angles)
        return self.serial.send_data(data)
        
