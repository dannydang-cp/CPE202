import unittest
from queue_array import *


class TestLab3(unittest. TestCase):

    def test_is_empty_true(self):
        """tests if the queue is empty"""
        queue = Queue(3)
        self.assertTrue(queue.is_empty())

    def test_is_empty_false(self):
        """tests if the queue is not empty"""
        queue = Queue(3)
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_is_full_true(self):
        """tests if the queue is full"""
        queue = Queue(2)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertTrue(queue.is_full())

    def test_is_full_false(self):
        """tests if the queue is not full"""
        queue = Queue(2)
        self.assertFalse(queue.is_full())

    def test_enqueue(self):
        """tests if items are added to the queue"""
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.queue, [1, 2, None])

    def test_enqueue_error(self):
        """tests if an index error ir raised when enqueueing a full list"""
        with self.assertRaises(IndexError):
            queue = Queue(1)
            queue.enqueue(1)
            queue.enqueue(2)

    def test_dequeue(self):
        """tests if first in item is removed and returned"""
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.queue, [None, 2, 3])

    def test_dequeue_error(self):
        """tests if an index error is raised when an empty queue is dequeued"""
        with self.assertRaises(IndexError):
            queue = Queue(3)
            queue.dequeue()

    def test_number_in_queue(self):
        """tests how many items are in the queue"""
        queue = Queue(3)
        queue.enqueue(5)
        self.assertEqual(queue.number_in_queue(), 1)
        queue.enqueue(7)
        self.assertEqual(queue.number_in_queue(), 2)
        queue.dequeue()
        self.assertEqual(queue.number_in_queue(), 1)


if __name__ == '__main__':
    unittest.main()
