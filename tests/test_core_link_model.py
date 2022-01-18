import unittest
import numpy as np

from core.link_model import Link


class TestLinkModel(unittest.TestCase):
    def test_create_link(self):
        l = Link(length=10)
        m = np.identity(4)
        n = np.array([
                [1, 0, 0, 10],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        np.testing.assert_array_equal(l.origin_matrix, m)
        np.testing.assert_array_equal(l.end_matrix, n)

    