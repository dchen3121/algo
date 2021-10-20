# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_max = float('-inf')
        result = float('-inf')
        for num in nums:
            curr_max = max(curr_max + num, num)  # we either include the prev part or not
            if curr_max > result:
                result = curr_max
        return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Naive 2 pointer approach iterates through all the points, but we don't need to
# Greedy approach allows us to quickly eliminate points we don't need
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test53(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertAlmostEqual(
            self.soln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6
        )

    def test_single(self):
        self.assertAlmostEqual(
            self.soln.maxSubArray([1]), 1
        )

    def test_positive(self):
        self.assertAlmostEqual(
            self.soln.maxSubArray([5,4,-1,7,8]), 23
        )

    def test_least_negative(self):
        self.assertAlmostEqual(
            self.soln.maxSubArray([-3,-1,-4,-5]), -1
        )

if __name__ == '__main__':
    unittest.main()
