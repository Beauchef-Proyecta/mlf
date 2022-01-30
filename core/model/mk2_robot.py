import numpy as np

from .robot_model import GenericRobot


class MK2Model:

    _build_instructions = {
        "link_0": {"length": 55, "axis": "z", "rotation": 0, "parent": None},
        "link_1": {"length": 39, "axis": "z", "rotation": 0, "parent": "link_0"},
        "link_2": {"length": 135, "axis": "y", "rotation": 0, "parent": "link_1"},
        "link_3": {
            "length": 147,
            "axis": "y",
            "rotation": 0 * np.pi / 180,
            "parent": "link_2",
        },
        "link_4": {"length": 66, "axis": "y", "rotation": 0, "parent": "link_3"},
    }

    def __init__(self):
        self.model = GenericRobot(self._build_instructions).assemble()

    def set_pose(self, q):
        q[0] = q[0] * np.pi / 180
        q[1] = q[1] * np.pi / 180
        q[2] = q[2] * np.pi / 180

        Q = dict()
        Q["link_0"] = 0
        Q["link_1"] = q[0]
        Q["link_2"] = q[1]
        Q["link_3"] = q[2]
        Q["link_4"] = np.pi / 2 - q[1] - q[2]

        self.model.set_pose(Q)

    def get_pose(self):
        return self.model.get_pose

    def inverse_kinematics(self, xyz: tuple[float]):
        q = []

        q[0] = np.arctan(y / x)
        q[2] = np.arccos(
            (
                (l1 * np.cos(q[0])) ** 2
                + (l2 * np.cos(q[0])) ** 2
                - (x - l3 * np.cos(q[0])) ** 2
                - (z - z0) ** 2
            )
            / (2 * l1 * l2 * (np.cos(q[0])) ** 2)
        )
        q[1] = -np.arctan((x - l3 * np.cos(q[0])) / (z - z0)) + np.arccos(
            (
                (l1 * np.cos(q[0])) ** 2
                + (x - l3 * np.cos(q[0])) ** 2
                + (z - z0) ** 2
                - (l2 * np.cos(q[0])) ** 2
            )
            / (2 * l1 * np.cos(q[0]) * np.sqrt(x ** 2 + z ** 2))
        )
        if z < 94:  # Experimentalmente funciona :)
            q[1] = q[1] - np.pi

        q0 = np.round(q[0] * 180 / np.pi, 0)
        q1 = np.round(q[1] * 180 / np.pi, 0)
        q2 = np.round(q[2] * 180 / np.pi, 0)
        return [q0, q1, q2]
