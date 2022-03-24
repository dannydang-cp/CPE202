import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_invalid(self):
        self.assertFalse(postfix_valid(""))
        self.assertFalse(postfix_valid("2 3"))
 
    def test_valid(self):
        self.assertTrue(postfix_valid("2 3 +"))
        self.assertTrue(postfix_valid("2 3 -"))
        self.assertTrue(postfix_valid("2 3 *"))
        self.assertTrue(postfix_valid("2 3 /"))

    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfixeval2(self):
        self.assertEqual(postfix_eval("5 4 -"), 1)

    def test_postfixeval3(self):
        self.assertEqual(postfix_eval("5 4 *"), 20)

    def test_postfixeval4(self):
        self.assertEqual(postfix_eval("10 2 /"), 5)

    def test_postfixeval5(self):
        self.assertEqual(postfix_eval("10 2 6 * + "), 22)

    def test_inToPostBasicAssoc(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_inToPostBasicAssoc1(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")

    def test_inToPostBasicAssoc2(self):
        self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")

    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")

    def test_inToPostBasicAssoc5(self):
        self.assertEqual(infix_to_postfix("6"), "6")
        with self.assertRaises(ValueError):
            postfix_eval("3 0 /")

    def test_infix_to_postfix_add_add(self):
        self.assertEqual(infix_to_postfix("6 + 3 + 2"), "6 3 + 2 +")

    def test_infix_to_postfix_add_sub(self):
        self.assertEqual(infix_to_postfix("6 + 3 - 2"), "6 3 + 2 -")

    def test_infix_to_postfix_add_multi(self):
        self.assertEqual(infix_to_postfix("6 + 3 * 2"), "6 3 2 * +")

    def test_infix_to_postfix_add_div(self):
        self.assertEqual(infix_to_postfix("6 + 4 / 2"), "6 4 2 / +")

    def test_infix_to_postfix_sub_sub(self):
        self.assertEqual(infix_to_postfix("6 - 4 - 2"), "6 4 - 2 -")

    def test_infix_to_postfix_sub_add(self):
        self.assertEqual(infix_to_postfix("6 - 4 + 2"), "6 4 - 2 +")

    def test_infix_to_postfix_sub_multi(self):
        self.assertEqual(infix_to_postfix("6 - 4 * 2"), "6 4 2 * -")

    def test_infix_to_postfix_sub_div(self):
        self.assertEqual(infix_to_postfix("6 - 4 / 2"), "6 4 2 / -")

    def test_infix_to_postfix_div_div(self):
        self.assertEqual(infix_to_postfix("8 / 2 / 4"), "8 2 / 4 /")

    def test_infix_to_postfix_div_multi(self):
        self.assertEqual(infix_to_postfix("8 / 2 * 4"), "8 2 / 4 *")

    def test_infix_to_postfix_div_add(self):
        self.assertEqual(infix_to_postfix("8 / 2 + 4"), "8 2 / 4 +")

    def test_infix_to_postfix_div_sub(self):
        self.assertEqual(infix_to_postfix("8 / 2 - 4"), "8 2 / 4 -")

    def test_infix_to_postfix_multi_multi(self):
        self.assertEqual(infix_to_postfix("8 * 2 * 4"), "8 2 * 4 *")

    def test_infix_to_postfix_multi_div(self):
        self.assertEqual(infix_to_postfix("8 * 2 / 4"), "8 2 * 4 /")

    def test_infix_to_postfix_multi_add(self):
        self.assertEqual(infix_to_postfix("8 * 2 + 4"), "8 2 * 4 +")

    def test_infix_to_postfix_multi_sub(self):
        self.assertEqual(infix_to_postfix("8 * 2 - 4"), "8 2 * 4 -")

    def test_infix_to_postfix_1(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"),
                         "3 4 2 * 1 5 - 2 3 ^ ^ / +")
if __name__ == "__main__":
    unittest.main()
