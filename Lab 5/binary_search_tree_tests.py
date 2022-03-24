import unittest
from binary_search_tree import *


class TestLab5(unittest.TestCase):
	def test_find_successors(self):
		a = BinarySearchTree()
		a.insert(3)
		a.insert(1)
		a.insert(10)
		a.insert(6)
		self.assertEqual(a.root.find_successor().key, 6)

