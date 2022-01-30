import unittest
import numpy as np

from core.model.robot_model import GenericRobot


class TestGenericRobot(unittest.TestCase):
    def test_create_single_link_robot(self):
        instructions = {
            "link_0": {"length": 1, "axis": "x", "rotation": 0, "parent": None},
        }

        r = GenericRobot(instructions).assemble()

        self.assertEqual(len(r.links), 1)
        np.testing.assert_equal(r.get_pose["link_0"][0], np.array([0, 0, 0]))
        np.testing.assert_equal(r.get_pose["link_0"][1], np.array([0, 0, 1]))

    def test_create_two_links_robot(self):
        instructions = {
            "link_0": {"length": 1, "axis": "x", "rotation": 0, "parent": None},
            "link_1": {"length": 1, "axis": "y", "rotation": 0, "parent": "link_0"},
        }

        r = GenericRobot(instructions).assemble()

        self.assertEqual(len(r.links), 2)
        self.assertEqual(r.links["link_0"], r.links["link_1"].parent)
        self.assertEqual(r.links["link_0"].child, r.links["link_1"])
        np.testing.assert_equal(r.get_pose["link_0"][0], np.array([0, 0, 0]))
        np.testing.assert_equal(r.get_pose["link_0"][1], np.array([0, 0, 1]))
        np.testing.assert_equal(r.get_pose["link_1"][0], np.array([0, 0, 1]))
        np.testing.assert_equal(r.get_pose["link_1"][1], np.array([0, 0, 2]))

    def test_rotate_three_links_robot(self):
        instructions = {
            "link_0": {"length": 1, "axis": "z", "rotation": 0, "parent": None},
            "link_1": {"length": 1, "axis": "y", "rotation": 0, "parent": "link_0"},
            "link_2": {"length": 1, "axis": "y", "rotation": 0, "parent": "link_1"},
        }

        r = GenericRobot(instructions).assemble()
        print(r.get_pose)
        r.set_pose({"link_0": np.pi / 2, "link_1": np.pi / 2, "link_2": np.pi / 2})
        print(r.get_pose)
        np.testing.assert_almost_equal(r.get_pose["link_0"][0], np.array([0, 0, 0]))
        np.testing.assert_almost_equal(r.get_pose["link_0"][1], np.array([0, 0, 1]))
        np.testing.assert_almost_equal(r.get_pose["link_1"][0], np.array([0, 0, 1]))
        np.testing.assert_almost_equal(r.get_pose["link_1"][1], np.array([0, 1, 1]))
        np.testing.assert_almost_equal(r.get_pose["link_2"][0], np.array([0, 1, 1]))
        np.testing.assert_almost_equal(r.get_pose["link_2"][1], np.array([0, 1, 0]))
