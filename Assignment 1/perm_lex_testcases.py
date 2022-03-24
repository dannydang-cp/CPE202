import unittest
from perm_lex import *


class TestAssignment1(unittest.TestCase):
    def test_perm_lex(self):
        """test if given an empty string to return an empty list"""
        self.assertEqual(perm_lex(''), [])

    def test_perm_lex1(self):
        """test if given a one character string to return the same character lilst"""
        self.assertEqual(perm_lex('a'), ['a'])

    def test_perm_lex2(self):
        """"test if the permutation in lex order of abc is correct"""
        self.assertEqual(perm_lex('abc'), ['abc', 'acb', 'bac', 'bca',
                                           'cab', 'cba'])
        """test if the permutation in lex order of abcd is correct"""
    def test_perm_lex3(self):
        self.assertEqual(perm_lex('abcd'), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                            'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                            'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                            'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])


if __name__ == "__main__":
    unittest.main()
