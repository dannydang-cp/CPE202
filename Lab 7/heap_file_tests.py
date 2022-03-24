import unittest
from heap_lab import *


class TestLab7(unittest.TestCase):

    def test_build_heap(self):
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        self.assertTrue(heap.build_heap(lst))
        self.assertEqual(heap.heap, [0, 5, 4, 3, 1, 2])

    def test_build_heap_false(self):
        heap = MaxHeap(1)
        lst = [1, 2]
        self.assertFalse(heap.build_heap(lst))

    def test_peek_self(self):
        # Test peek function
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        heap.build_heap(lst)
        self.assertEqual(heap.peek(), 5)

    def test_peek_error(self):
        # Test peek function error
        heap = MaxHeap()
        with self.assertRaises(IndexError):
            heap.peek()

    def test_enqueue_perc_up(self):
        # Test enqueue
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        heap.build_heap(lst)
        heap.enqueue(6)
        self.assertEqual(heap.heap, [0, 6, 4, 5, 1, 2, 3])

    def test_enqueue_False(self):
        # Test enqueue False
        heap = MaxHeap(1)
        heap.enqueue(6)
        self.assertFalse(heap.enqueue(7))

    def test_dequeue(self):
        # Test dequeue
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        heap.build_heap(lst)
        heap.dequeue()
        self.assertEqual(heap.heap, [0, 4, 2, 3, 1])

    def test_dequeue_error(self):
        heap = MaxHeap()
        with self.assertRaises(IndexError):
            heap.dequeue()

    def test_contents(self):
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        heap.build_heap(lst)
        self.assertEqual(heap.contents(), [0, 5, 4, 3, 1, 2])

    def test_is_empty_true(self):
        heap = MaxHeap()
        self.assertTrue(heap.is_empty())

    def test_is_empty_false(self):
        heap = MaxHeap()
        heap.enqueue(1)
        self.assertFalse(heap.is_empty())

    def test_is_full_true(self):
        heap = MaxHeap(1)
        heap.enqueue(1)
        self.assertTrue(heap.is_full())

    def test_is_full_false(self):
        heap = MaxHeap()
        self.assertFalse(heap.is_full())

    def test_size(self):
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        heap.build_heap(lst)
        self.assertEqual((heap.size()), 5)

    def test_heap_sort_ascending(self):
        heap = MaxHeap()
        lst = [1, 2, 3, 4, 5]
        heap.build_heap(lst)
        a_list = [2, 5, 6, 3, 1, 10, 15]
        self.assertEqual(heap.heap_sort_ascending(a_list), [0, 1, 2, 3, 5, 6, 10, 15])

