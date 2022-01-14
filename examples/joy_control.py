# import sys
# sys.path.append('/home/pi/mlf/core')
# from serial_control import Serial_control
# from mk2robot import MK2Robot
from core.serial_control import SerialControl  # for pc
from core.mk2robot import MK2Robot  # for pc
from pynput import keyboard

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot_serial = SerialControl("COM5")
robot_serial.open_serial()
pose = 45
pose2 = 90
pose3 = 90


try:
    while True:
        print(" ")
        with keyboard.Events() as events:
            # Block for as much as possible
            event = events.get(1e6)
            if event.key == keyboard.KeyCode.from_char('a'):
                pose = pose - 2
                robot_serial.write_servo(1, pose)
                if pose < 0:
                    pose = 0
                    pass

            if event.key == keyboard.KeyCode.from_char('d'):
                pose = pose + 2
                robot_serial.write_servo(1, pose)
                if pose > 90:
                    pose = 90
                    pass

            if event.key == keyboard.KeyCode.from_char('w'):
                pose2 = pose2 + 2
                robot_serial.write_servo(2, pose2)
                if pose2 > 150:
                    pose2 = 150
                    pass

            if event.key == keyboard.KeyCode.from_char('s'):
                pose2 = pose2 - 2
                robot_serial.write_servo(2, pose2)
                if pose2 < 40:
                    pose2 = 40
                    pass

            if event.key == keyboard.KeyCode.from_char('q'):
                pose3 = pose3 + 2
                robot_serial.write_servo(3, pose3)
                if pose3 > 120:
                    pose3 = 120
                    pass

            if event.key == keyboard.KeyCode.from_char('e'):
                pose3 = pose3 - 2
                robot_serial.write_servo(3, pose3)
                if pose3 < 60:
                    pose3 = 60
                    pass
except KeyboardInterrupt:
    pass