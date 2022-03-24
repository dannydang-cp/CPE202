import unittest
from ordered_list import *


class TestLab4(unittest. TestCase):

    def test_add_remove(self):
        """"Tests if the items added are correctly added and are in the right order.
        Items removed are also tested and are checked if the list decreasing correctly"""
        lst = OrderedList()
        lst.add(3)
        lst.add(1)
        lst.add(2)
        self.assertEqual(repr(lst), '[1, 2, 3]')
        lst.remove(3)
        self.assertEqual(repr(lst), '[1, 2]')
        lst.remove(1)
        self.assertEqual(repr(lst), '[2]')

    def test_search_forward_backward(self):
        """Tests if the items founded or not founded returns the correct boolean"""
        lst = OrderedList()
        lst.add(1)
        lst.add(9)
        lst.add(4)
        self.assertTrue(lst.search_forward(9))
        self.assertFalse(lst.search_forward(3))
        self.assertTrue(lst.search_backward(1))
        self.assertFalse(lst.search_backward(2))

    def test_is_empty_true(self):
        """Tests if the correct boolean is returned when the list is empty"""
        lst = OrderedList()
        self.assertTrue(lst.is_empty())

    def test_is_empty_false(self):
        """Tests if the correct boolean is returned when the list is not empty"""
        lst = OrderedList()
        lst.add(1)
        self.assertFalse(lst.is_empty())

    def test_size(self):
        """Tests if the size of the list is the correct size"""
        lst = OrderedList()
        lst.add(1)
        self.assertEqual(lst.size(), 1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(lst.size(), 3)

    def test_index(self):
        """Tests if the index function finds the correct index of where the item is """
        lst = OrderedList()
        lst.add(1)
        lst.add(3)
        lst.add(5)
        self.assertEqual(lst.index(1), 0)
        self.assertEqual(lst.index(3), 1)
        self.assertEqual(lst.index(5), 2)

    def test_pop(self):
        """Tests if the last item in the list is correctly popped and the list is in the right order"""
        lst = OrderedList()
        lst.add(1)
        lst.add(2)
        lst.add(3)
        self.assertEqual(lst.pop(), 3)
        self.assertEqual(lst.pop(), 2)
        self.assertEqual(lst.pop(), 1)

    def test_pop_pos(self):
        """Tests if the item at the position is correctly popped and the list is in the right order afterwards"""
        lst = OrderedList()
        lst.add(5)
        lst.add(3)
        lst.add(8)
        lst.add(15)
        lst.add(1)
        lst.pop_pos(2)
        self.assertEqual(repr(lst), "[1, 3, 8, 15]")
        lst.pop_pos(3)
        self.assertEqual(repr(lst), "[1, 3, 8]")
        lst.pop_pos(0)
        self.assertEqual(repr(lst), "[3, 8]")
