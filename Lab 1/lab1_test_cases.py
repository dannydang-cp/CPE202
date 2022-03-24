import unittest
from lab1 import *


class TestLab1(unittest.TestCase):
    def test_max_list_iter(self):
        """test if the function returns a ValueError when list is empty"""
        test_list = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(test_list)

    def test_max_list_iter1(self):
        """tests if the function can find the max at the end boundary"""
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_list_iter(test_list), 5)

    def test_max_list_iter2(self):
        """test if the function can find the max at the start boundary"""
        test_list = [5, 4, 3 ,2, 1]
        self.assertEqual(max_list_iter(test_list), 5)

    def test_max_list_iter3(self):
        """test if the function can find the max in the middle"""
        test_list = [1, 2, 5, 3, 4]
        self.assertEqual(max_list_iter(test_list), 5)

    def test_reverse_rec(self):
        """test if the function reverses the list"""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec1(self):
        """test if the function reverses a non linear list"""
        self.assertEqual(reverse_rec([5, 3, 1]), [1, 3, 5])

    def test_reverse_rec2(self):
        """test if the function gives a ValueError when list is empty"""
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        """test if the function finds the index number in the middle of the list"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search1(self):
        """test if the function finds the index number at the start of the list"""
        test_list = [1, 2, 4, 8, 10, 15]
        self.assertEqual(bin_search(1, 0, len(test_list) - 1, test_list), 0)

    def test_bin_search2(self):
        """test if the function finds the index number at the end of the list"""
        test_list = [1, 2, 4, 8, 10, 15]
        self.assertEqual(bin_search(15, 0, len(test_list) - 1, test_list), 5)

    def test_bin_search3(self):
        """test if the function raises a ValueError if target is not in list"""
        test_list = [0, 1, 2, 3, 4]
        with self.assertRaises(ValueError):
            bin_search(5, 0, len(test_list) - 1, test_list)

if __name__ == "__main__":
        unittest.main()
