import unittest
from serial import Serial
from mock_serial import MockSerial

from core.serial_wrapper.serial_control import SerialController
from core.serial_wrapper.mk2_serial import MK2Serial


class TestSerial(unittest.TestCase):
    # def test_serial_controller(self):
    #     device = MockSerial()
    #     device.open()
    #     stub = device.stub(receive_bytes=b'10A0A0A0', send_bytes=b'E')

    #     serial_controller = SerialController(device.port)
    #     serial_controller.serial = Serial(device.port)
        
    #     robot = MK2Serial()
    #     robot.serial = serial_controller

    #     # device.close()
    #     data = robot.serial.build_serial_msg(0xA0, [0xA0,0xA0,0xA0])
    #     print(data)
    #     # response = robot.set_joints([10,10,10])
    #     assert False
    #     self.assertTrue(stub.called)
    #     self.assertEqual(stub.call(), response)

    
