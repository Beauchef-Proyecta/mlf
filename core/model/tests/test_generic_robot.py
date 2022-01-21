import unittest
import numpy as np

from core.model.generic_robot import GenericRobot


class TestGenericRobot(unittest.TestCase):
    def test_create_single_link_robot(self):
        instructions = {
            0: {"length": 1, "axis": "x", "rotation": 0, "parent": None},
        }

        r = GenericRobot(instructions).assemble()

        self.assertEqual(len(r._links), 1)
        np.testing.assert_equal(r.get_pose[0], np.array([0, 0, 1]))

    def test_create_two_links_robot(self):
        instructions = {
            0: {"length": 1, "axis": "x", "rotation": 0, "parent": None},
            1: {"length": 1, "axis": "y", "rotation": 0, "parent": 0},
        }

        r = GenericRobot(instructions).assemble()

        self.assertEqual(len(r._links), 2)
        self.assertEqual(r._links[0], r._links[1].parent)
        self.assertEqual(r._links[0].child, r._links[1])
        np.testing.assert_equal(r.get_pose[0], np.array([0, 0, 1]))
        np.testing.assert_equal(r.get_pose[-1], np.array([0, 0, 2]))

    def test_rotate_three_links_robot(self):
        instructions = {
            0: {"length": 1, "axis": "z", "rotation": 0, "parent": None},
            1: {"length": 1, "axis": "y", "rotation": 0, "parent": 0},
            2: {"length": 1, "axis": "y", "rotation": 0, "parent": 1},
        }

        r = GenericRobot(instructions).assemble()
        print(r.get_pose)
        r.set_pose([np.pi / 2, np.pi / 2, np.pi / 2])
        print(r.get_pose)
        np.testing.assert_almost_equal(r.get_pose[0], np.array([0, 0, 1]))
        np.testing.assert_almost_equal(r.get_pose[1], np.array([0, 1, 1]))
        np.testing.assert_almost_equal(r.get_pose[2], np.array([0, 1, 0]))
