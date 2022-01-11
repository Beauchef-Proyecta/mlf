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
        p = translation_along_zaxis(0)
        q = translation_along_zaxis(1)
        np.testing.assert_array_equal(np.dot(p,q), q)

if __name__ == "__main__":
    unittest.main()
