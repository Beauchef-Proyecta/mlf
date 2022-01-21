import numpy as np

from .generic_robot import GenericRobot


class MK2Robot:
    def __init__(self):
        self._build_instructions = {
            0: {"length": 55, "axis": "z", "rotation": 0, "parent": None},
            1: {"length": 39, "axis": "z", "rotation": 0, "parent": 0},
            2: {"length": 135, "axis": "y", "rotation": 0, "parent": 1},
            3: {"length": 147, "axis": "y", "rotation": 0 * np.pi/180, "parent": 2},
            4: {"length": 66, "axis": "y", "rotation": 0, "parent": 3},
        }

        self.model = GenericRobot(self._build_instructions).assemble()
        self._home = []
        self._limits = []

    def set_pose(self, q):
        q[0] = q[0] * np.pi / 180
        q[1] = q[1] * np.pi / 180
        q[2] = q[2] * np.pi / 180

        Q = [0] * 5
        Q[0] = 0
        Q[1] = q[0]
        Q[2] = q[1]
        Q[3] = q[2]
        Q[4] = np.pi / 2 - q[1] - q[2]

        self.model.set_pose(Q)
    
    def get_pose(self):
        return list(self.model.get_pose)

    def check_limits(self):
        pass
