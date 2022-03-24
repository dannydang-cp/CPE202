import unittest
from stack_nodelist import *


class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self):
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self):
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_is_empty_true(self):
        """tests if the stack is empty"""
        stack = Stack()
        self.assertTrue(Stack.is_empty(stack))

    def test_is_empty_false(self):
        """tests if the stack is not empty"""
        stack = Stack()
        stack.push(1)
        self.assertFalse(Stack.is_empty(stack))

    def test_push(self):
        """tests if the item is pushed onto the stack"""
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top.value, 1)
        stack.push(2)
        self.assertEqual(stack.top.value, 2)
        self.assertEqual(stack.top.rest.value, 1)

    def test_pop(self):
        """tests if the most recent item is popped and returned from the stack"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.top, Node(1, None))
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.top, None)

    def test_pop_error(self):
        """tests if an index error is raised when an empty stack is popped"""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        """tests if the most recent item is returned """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_peek_error(self):
        """tests if an index error is raised an empty stack is peeked"""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size(self):
        """tests the size of the stack"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)


if __name__ == '__main__':
    unittest.main()
