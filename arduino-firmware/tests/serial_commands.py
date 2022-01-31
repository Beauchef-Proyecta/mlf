import numpy as np

from core.serial import MK2Serial


if __name__ == "__main__":
    mk2 = MK2Serial()
    mk2.open()
    i = 0
    while True:
        i += 2
        angle1 = int((90 * np.sin(i * np.pi / 180)) + 90) & 0xFF
        angle2 = int((30 * np.sin(2 * i * np.pi / 180)) + 90) & 0xFF
        angle3 = int((30 * np.sin(i * np.pi / 180)) + 90) & 0xFF
        i %= 360

        data = mk2.build_serial_msg(0x10, [angle1, angle2, angle3])
        s = mk2.send_data(data)
        print(f"[{i}: {angle1}]->{s}")
