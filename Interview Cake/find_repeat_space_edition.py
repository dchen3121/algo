# We have a list of integers, where:
# 1. The integers are in the range 1..n
# 2. The list has a length of n+1
# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.
# Write a function which finds an integer that appears more than once in our list. Don't modify the input.
# If there are multiple duplicates, you only need to find one of them.
# The catch: you need to optimize space! Time is not that big of a concern


from typing import List
from typing_extensions import ParamSpecArgs


def find_duplicate(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    floor, ceil = 0, len(sorted_nums) - 1
    while floor <= ceil:
        if floor == ceil:
            return sorted_nums[floor]
        mid = (floor + ceil) // 2
        num_at_mid = sorted_nums[mid]
        if num_at_mid <= mid:
            ceil = mid - 1
        else:
            floor = mid + 1
    return sorted_nums[floor]




# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# since time is not a concern, we can sort the list first, then perform binary search
# 1, 2, 3, 4, 5, 5  -> if the number on the index is less than the index, search left
# 1, 2, 3, 4, 5, 5, 6  -> if the number on the index is greater or eql to the index, search right
# O(1) space, O(n log n) time
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            find_duplicate([1, 2, 3, 4, 5, 5, 6]),
            5
        )

    def test_general_2(self):
        self.assertEqual(
            find_duplicate([1, 2, 3, 4, 5, 5, 6, 7, 8, 9]),
            5
        )

    def test_general_3(self):
        self.assertEqual(
            find_duplicate([1, 2, 3, 4, 5, 6, 7, 2, 8, 9]),
            2
        )

if __name__ == '__main__':
    unittest.main()
