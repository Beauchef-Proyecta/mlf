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
        p = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        q = np.array([
                [1, 0, 0, 1],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        Tz = translation_along_x(1)
        print(Tz)
        np.testing.assert_array_equal(np.dot(Tz, p), q)

    def test_translation_along_y(self):
        p = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        q = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

        Ty = translation_along_y(1)
        np.testing.assert_array_equal(np.dot(Ty, p), q)

    def test_translation_along_z(self):
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

        Tz = translation_along_z(1)
        np.testing.assert_array_equal(np.dot(Tz, p), q)
   
    def test_rotate_aroun_x(self):
        p = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ])

        q = np.array([
                [1, 0, 0, 0],
                [0, np.sqrt(2)/2, -np.sqrt(2)/2, 0],
                [0, np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2],
                [0, 0, 0, 1]
            ])

        Rx = rotation_around_x(np.pi/4)
        np.testing.assert_array_almost_equal(np.dot(Rx, p), q)

    def test_rotate_aroun_y(self):
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

        Ry = rotation_around_y(np.pi)
        np.testing.assert_array_almost_equal(np.dot(Ry, p), q)


    def test_rotate_around_z(self):
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

        Rz = rotation_around_z(np.pi)
        np.testing.assert_array_almost_equal(np.dot(Rz, p), q)

if __name__ == "__main__":
    unittest.main()
