import unittest
from sorts import *


class TestLab6(unittest.TestCase):

    def test_01_selection(self):
        nums = [23, 10, 49, 12]
        comps = selection_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [10, 12, 23, 49])

    def test_02_selection(self):
        nums = [12, 5, 6, 2, 18]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [2, 5, 6, 12, 18])

    def test_01_insertion(self):
        nums = [12, 5, 6, 2, 18]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 7)
        self.assertEqual(nums, [2, 5, 6, 12, 18])

    def test_02_insertion(self):
        nums = [23, 10, 49, 31]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 4)
        self.assertEqual(nums, [10, 23, 31, 49])

    def test_03_insertion(self):
        nums = [2, 6, 5, 1, 3, 4]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 12)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

    def test_04_insertion(self):
        nums = [10, 8, 6, 4]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [4, 6, 8, 10])


    def test_03_selection_sort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            selection_sort(randoms)
            self.assertEqual(randoms, expected)

    def test_04_insertion_sort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            insertion_sort(randoms)
            self.assertEqual(randoms, expected)

    def test_05_selection_sort_number_of_comps(self):
        n = 100
        randoms = random.sample(range(1000000), n)
        comps = selection_sort(randoms)

        self.assertEqual(comps, 4950)

    def test_06_insertion_sort_number_of_comps(self):
        nums = []
        for i in range(50):
            nums.append(i*2)
            nums.append((50-i)*2-1)
        comps = insertion_sort(nums)
        self.assertEqual(comps, 2574)
        comps = insertion_sort(nums)
        self.assertEqual(comps, 99)
        nums.sort(reverse=True)
        comps = insertion_sort(nums)
        self.assertEqual(comps, 4950)

    def test_01_merge_sort(self):
        nums = [21, 38, 29, 17]
        comps = merge_sort(nums)
        self.assertEqual(comps, 5)
        self.assertEqual(nums, [17, 21, 29, 38])

    def test_02_merge_sort(self):
        nums = [21, 38, 29, 17, 4, 25, 32, 9]
        comps = merge_sort(nums)
        self.assertEqual(comps, 17)
        self.assertEqual(nums, [4, 9, 17, 21, 25, 29, 32, 38])

    def test_03_merge_sort(self):
        nums = [2, 6, 5, 1, 7, 4, 3]
        comps = merge_sort(nums)
        self.assertEqual(comps, 13)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
