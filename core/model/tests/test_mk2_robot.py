import unittest
import numpy as np

from core.model import MK2Model


class TestMK2Model(unittest.TestCase):
    def test_setup_robot(self):
        r = MK2Model()
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0, 0, 55),
            "link_1": (0, 0, 94),
            "link_2": (0, 0, 229),
            "link_3": (147, 0, 229),
            "link_4": (213, 0, 229),
        }

        for name, (origin, end) in pose.items():
            np.testing.assert_almost_equal(end, desired_pose[name])

    def test_turn_left(self):
        r = MK2Model()
        r.set_pose(q0=45)
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0, 0, 55),
            "link_1": (0, 0, 94),
            "link_2": (0, 0, 229),
            "link_3": (147 * np.sqrt(2) / 2, 147 * np.sqrt(2) / 2, 229),
            "link_4": (213 * np.sqrt(2) / 2, 213 * np.sqrt(2) / 2, 229),
        }

        for name, (origin, end) in pose.items():
            np.testing.assert_almost_equal(end, desired_pose[name])

    def test_turn_right(self):
        r = MK2Model()
        r.set_pose(q0=-45)
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0, 0, 55),
            "link_1": (0, 0, 94),
            "link_2": (0, 0, 229),
            "link_3": (147 * np.sqrt(2) / 2, -147 * np.sqrt(2) / 2, 229),
            "link_4": (213 * np.sqrt(2) / 2, -213 * np.sqrt(2) / 2, 229),
        }

        for name, (origin, end) in pose.items():
            np.testing.assert_almost_equal(end, desired_pose[name])

    def test_arbitraty_position_1(self):
        r = MK2Model()
        r.set_pose(q0=0, q1=30, q2=90)
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0.0, 0.0, 55.0),
            "link_1": (0.0, 0.0, 94.0),
            "link_2": (67.5, 0.0, 210.91),
            "link_3": (194.81, 0.0, 137.41),
            "link_4": (260.81, 0.0, 137.41),
        }

        for name, (origin, end) in pose.items():
            print(f'"{name}": {tuple(end)},')
            np.testing.assert_almost_equal(end, desired_pose[name], decimal=2)

    def test_arbitraty_position_2(self):
        r = MK2Model()
        r.set_pose(q0=15, q1=30, q2=120)
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0.0, 0.0, 55.0),
            "link_1": (0.0, 0.0, 94.0),
            "link_2": (65.20, 17.47, 210.91),
            "link_3": (136.20, 36.49, 83.61),
            "link_4": (199.95, 53.58, 83.61),
        }

        for name, (origin, end) in pose.items():
            print(f'"{name}": {tuple(end)},')

        for name, (origin, end) in pose.items():
            np.testing.assert_almost_equal(end, desired_pose[name], decimal=2)

    def test_arbitraty_position_3(self):
        r = MK2Model()
        r.set_pose(q0=60, q1=-45, q2=20)
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0.0, 0.0, 55.0),
            "link_1": (0.0, 0.0, 94.0),
            "link_2": (-47.73, -82.67, 189.46),
            "link_3": (-78.79, -136.47, 322.69),
            "link_4": (-45.79, -79.31, 322.69),
        }

        for name, (origin, end) in pose.items():
            print(f'"{name}": {tuple(end)},')

        for name, (origin, end) in pose.items():
            np.testing.assert_almost_equal(end, desired_pose[name], decimal=2)

    def test_arbitraty_position_4(self):
        r = MK2Model()
        r.set_pose(q0=-27, q1=45, q2=0)
        pose = r.get_pose()

        desired_pose = {
            "link_0": (0.0, 0.0, 55.0),
            "link_1": (0.0, 0.0, 94.0),
            "link_2": (85.05, -43.34, 189.46),
            "link_3": (177.67, -90.53, 293.40),
            "link_4": (236.48, -120.49, 293.40),
        }

        for name, (origin, end) in pose.items():
            np.testing.assert_almost_equal(end, desired_pose[name], decimal=2)

    def test_inverse_kinematics_2(self):
        q = (15, 30, 120)
        xyz = (199.95, 53.58, 83.61)
        r = MK2Model()
        ik = np.array(r.inverse_kinematics(xyz))

        np.testing.assert_almost_equal(ik, q)

    def test_inverse_kinematics_4(self):
        q = (-27, 45, 0)
        xyz = (236.48, -120.49, 293.40)
        r = MK2Model()
        ik = np.array(r.inverse_kinematics(xyz))

        np.testing.assert_almost_equal(ik, q)
