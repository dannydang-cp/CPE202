import unittest
from stack_array import Stack


class TestLab2(unittest.TestCase):
    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_is_empty_true(self):
        """Tests if the stack is empty"""
        stack = Stack(1)
        self.assertTrue(stack.is_empty())

    def test_is_empty_false(self):
        """Tests if the stack is not empty"""
        stack = Stack(1)
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_is_full_true(self):
        """Tests if the stack is full"""
        stack = Stack(1)
        stack.push(1)
        self.assertTrue(stack.is_full())

    def test_is_full_false(self):
        """"Tests if the stack is not full"""
        stack = Stack(1)
        self.assertFalse(stack.is_full())

    def test_push(self):
        """Tests if items are pushed onto the stack"""
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.items, [1, 2, 3])

    def test_push_error(self):
        """Tests if an index error is raised when trying to push onto a full stack"""
        stack = Stack(1)
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(2)

    def test_pop(self):
        """Tests if the most recent item pushed is removed and returned"""
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.items, [1, 2, None])

    def test_pop_error(self):
        """Tests if an index error is raised when trying to pop an empty stack"""
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        """Tests if the most recent items is returned"""
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)

    def test_peek_error(self):
        """Tests if an index error is raised when trying to peek an empty stack"""
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size(self):
        """Tests the size of the stack"""
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)


if __name__ == '__main__':
    unittest.main()
