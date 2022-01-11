import unittest
import numpy as np

from core.mk2robot import (
    translation_along_zaxis,
    rotation_around_yaxis,
    rotation_around_zaxis,
    MK2Robot
)

class TestTransformationMatrices(unittest.TestCase):
    def test_translation_along_zaxis(self):
        p = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        q = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ])

        Tz = translation_along_zaxis(1)
        np.testing.assert_array_equal(np.dot(p,Tz), q)

    
    def test_rotate_aroung_yaxis(self):
        p = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ])

        q = np.array([
                [-1, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, -1, -1],
                [0, 0, 0, 1]
            ])

        Ry = rotation_around_yaxis(np.pi)
        np.testing.assert_array_almost_equal(np.dot(Ry,p), q)


    def test_rotate_aroung_zaxis(self):
        p = np.array([
                [1, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ])

        q = np.array([
                [-1, 0, 0, -1],
                [0, -1, 0, -1],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ])

        Rz = rotation_around_zaxis(np.pi)
        np.testing.assert_array_almost_equal(np.dot(Rz,p), q)

if __name__ == "__main__":
    unittest.main()
