import unittest
import numpy as np

from core.transformations import (
                        rotation_around_x, 
                        rotation_around_y, 
                        rotation_around_z,
                        translation_along_x,
                        translation_along_y,
                        translation_along_z
                        )

class TestTransformationMatrices(unittest.TestCase):
    def test_translation_along_x(self):
        p = np.array([0, 0, 0, 1])
        q = np.array([1, 0, 0, 1])
        Tz = translation_along_x(p, 1)
        np.testing.assert_array_equal(Tz, q)

    def test_translation_along_y(self):
        p = np.array([0, 0, 0, 1])
        q = np.array([0, 1, 0, 1])

        Ty = translation_along_y(p, 1)
        np.testing.assert_array_equal(Ty, q)

    def test_translation_along_z(self):
        p = np.array([0, 0, 0, 1])
        q = np.array([0, 0, 1, 1])

        Tz = translation_along_z(p, 1)
        np.testing.assert_array_equal(Tz, q)
   
    def test_rotate_around_x(self):
        p = np.array([0, 1, 1, 1])
        q = np.array([0, 0, np.sqrt(2), 1])

        Rx = rotation_around_x(p, np.pi/4)
        np.testing.assert_array_almost_equal(Rx, q)

    def test_rotate_around_y(self):
        p = np.array([0, 1, 1, 1])
        q = np.array([np.sqrt(2)/2, 1, np.sqrt(2)/2, 1])

        Ry = rotation_around_y(p, np.pi/4)
        np.testing.assert_array_almost_equal(Ry, q)


    def test_rotate_around_z(self):
        p = np.array([1, 1, 1, 1])
        q = np.array([-1, 1, 1, 1])

        Rz = rotation_around_z(p, np.pi/2)
        np.testing.assert_array_almost_equal(Rz, q)
