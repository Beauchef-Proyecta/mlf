import unittest
import numpy as np

from core.link_model import Link


class TestLinkModel(unittest.TestCase):
    def test_create_zero_link(self):
        l = Link(length=0, default_axis='x')
        m = np.array([0, 0, 0])
        n = np.array([0, 0, 0])
        self.assertEqual(l.lenght, 0)
        self.assertEqual(l.rotation, 0)
        np.testing.assert_array_equal(l.origin, m)
        np.testing.assert_array_equal(l.end, n)
        np.testing.assert_array_equal(l.base, np.identity(3))

    def test_create_non_zero_link(self):
        l = Link(length=10, default_axis='x')
        m = np.array([0, 0, 0])
        n = np.array([0, 0, 10])
        np.testing.assert_array_equal(l.origin, m)
        np.testing.assert_array_equal(l.end, n)
        self.assertEqual(l.lenght, 10)
        self.assertEqual(l.rotation, 0)
        np.testing.assert_array_equal(l.base, np.identity(3))

    def test_create_link_invalid_axis(self):
        self.assertRaises(ValueError, Link, 10, 'a')
    
    def test_rotate_link_around_x(self):
        l = Link(length=1, default_axis='x', rotation=np.pi/4)
        np.testing.assert_almost_equal(l.origin, np.array([0,0,0]))
        np.testing.assert_almost_equal(l.end, np.array([0,-np.sqrt(2)/2,np.sqrt(2)/2]))

    def test_rotate_link_around_y(self):
        l = Link(length=1, default_axis='y')
        l.set_pose(np.pi/4)
        np.testing.assert_almost_equal(l.origin, np.array([0,0,0]))
        np.testing.assert_almost_equal(l.end, np.array([np.sqrt(2)/2,0,np.sqrt(2)/2]))
    
    def test_rotate_link_around_z(self):
        l = Link(length=1, default_axis='z')
        n = np.array([0, 0, 1])
        l.set_pose(np.pi/4)
        np.testing.assert_array_almost_equal(l.end, n)
    
    def test_link_with_three_children(self):
        j = Link(length=1.0, default_axis='z')
        k = Link(length=1.0, default_axis='y')
        l = Link(length=1.0, default_axis='x')
        k.set_parent(j)
        l.set_parent(k)
        np.testing.assert_array_almost_equal(j.end, np.array([0, 0, 1.0]))
        np.testing.assert_array_almost_equal(k.end, np.array([0, 0, 2.0]))
        np.testing.assert_array_almost_equal(l.end, np.array([0, 0, 3.0]))

    def test_link_with_child_and_rotation(self):
        k = Link(length=1, default_axis='y')
        l = Link(length=1, default_axis='x')
        l.set_parent(k)
        np.testing.assert_array_almost_equal(k.end, np.array([0, 0, 1]))
        np.testing.assert_array_almost_equal(l.end, np.array([0, 0, 2]))
        
        k.set_pose(np.pi/2)
        np.testing.assert_array_equal(k.origin, np.array([0, 0, 0]))
        np.testing.assert_array_almost_equal(k.end, np.array([1, 0, 0]))
        np.testing.assert_array_almost_equal(l.end, np.array([2, 0, 0]))

        l.set_pose(np.pi/4)
        self.assertEqual(l._rotation, np.pi/4)
        np.testing.assert_array_equal(k.end, l.origin)
        np.testing.assert_array_almost_equal(l.end, np.array([1+np.sqrt(2)/2, -np.sqrt(2)/2, 0]))





        

    