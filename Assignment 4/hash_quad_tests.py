import unittest
from hash_quad import *

class TestAssignment4(unittest.TestCase):
    def test(self):
        hash = HashTable(10)
        hash.insert("hello", 5)
        print(hash.hash_table)
        self.assertEqual(hash.get_table_size(), 10)
        self.assertEqual(hash.get_num_items(), 1)
        self.assertEqual(hash.get_load_factor(), 0.1)
        self.assertEqual(hash.get_all_keys(), ["hello"])
        self.assertTrue(hash.in_table("hello"))
        self.assertFalse(hash.in_table("hi"))
        self.assertEqual(hash.get_index("hello"), 2)