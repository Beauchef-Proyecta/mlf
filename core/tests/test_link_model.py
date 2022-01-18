import unittest
import numpy as np

from core.link_model import Link


class TestLinkModel(unittest.TestCase):
    def test_create_zero_link(self):
        l = Link(length=10, axis='x')
        m = np.array([0, 0, 0, 1])
        n = np.array([10, 0, 0, 1])
        np.testing.assert_array_equal(l._origin, m)
        np.testing.assert_array_equal(l._end, n)
    
    def test_rotate_link_around_x(self):
        l = Link(length=1, axis='x', rotation=np.pi)
        np.testing.assert_almost_equal(l.origin, np.array([0,0,0]))
        np.testing.assert_almost_equal(l.end, np.array([1,0,0]))

    def test_rotate_link_around_y(self):
        l = Link(length=1, axis='y')
        l.set_pose(np.pi)
        np.testing.assert_almost_equal(l.origin, np.array([0,0,0]))
        np.testing.assert_almost_equal(l.end, np.array([-1,0,0]))
    
    def test_rotate_link_around_y(self):
        l = Link(length=1, axis='z')
        n = np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0, 1])
        l.set_pose(np.pi/4)
        np.testing.assert_array_almost_equal(l._end, n)
        np.testing.assert_array_almost_equal(l.end, np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]))

    def test_link_with_parent(self):
        l = Link(length=1, axis='x')
        k = Link(length=1, axis='y', rotation=np.pi/2, parent=l)
        np.testing.assert_array_equal(l.origin, np.array([0, 0, 0]))
        np.testing.assert_array_equal(l.end, np.array([1, 0, 0]))
        np.testing.assert_array_equal(l.end, k.origin)
        self.assertEqual(k._rotation, np.pi/2)
        np.testing.assert_array_equal(k.end, np.array([1, 0, -1]))




        

    