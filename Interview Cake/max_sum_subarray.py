# Given a n-length array of integers, find the maximum sum you can get from a subarray of the array.

# Example:
# input: [-2,1,-3,4,-1,2,1,-5,4]
# output: 6


from typing import List


def max_sum_subarray(nums: List[int]) -> int:
    if not nums:
        return 0

    max_sum = float('-inf')
    max_sum_including_curr = float('-inf')

    for num in nums:
        max_sum_including_curr = max(num, max_sum_including_curr + num)
        max_sum = max(max_sum, max_sum_including_curr)

    return max_sum


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Greedy approach - keep track of max sum so far + max sum including curr num. O(n) where n is length of prices list
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6
        )

if __name__ == '__main__':
    unittest.main()

