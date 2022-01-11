# Given a n-length array of integers, find the maximum product you can get from multiplying any k numbers in the array.

# Example:
# input: [-2,1,-3,4,-1,2,1,-5,4], 3
# output: 60


from typing import List


def max_product_of_k(nums: List[int], k: int) -> int:
    def product(start, end):
        result = 1
        while start < end:
            result *= nums[start]
            start += 1
        return result

    if len(nums) < k:
        raise Exception

    max_product_of_i = [product(0, i) for i in range(1, k + 1)]
    min_product_of_i = [product(0, i) for i in range(1, k + 1)]

    for i, num in enumerate(nums):
        # print(num)
        for j in range(k - 1, -1, -1):
            if j == 0:
                max_product_of_i[j] = max(max_product_of_i[j], num)
                min_product_of_i[j] = min(min_product_of_i[j], num)
            elif i > j:
                max_product_of_i[j] = max(
                    max_product_of_i[j],
                    max_product_of_i[j - 1] * num,
                    min_product_of_i[j - 1] * num
                )
                min_product_of_i[j] = min(
                    min_product_of_i[j],
                    max_product_of_i[j - 1] * num,
                    min_product_of_i[j - 1] * num
                )
        # print(max_product_of_i)
        # print(min_product_of_i)

    return max_product_of_i[-1]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
#
# Start simple - for 3
# Max product of 3 can be:
# - 3 greatest positive numbers
# - 2 most negative numbers + 1 greatest positive number
# - or, in the case where only negative numbers are present, 3 least negative numbers
#
# Hmm ... Seems like we can brute force our way through this one,
# but for larger numbers there will be too many of these magical cases that we need to consider
#
# Another possible solution: greedy
# For 3, keep track of:
# - most negative
# - most positive
# - highest positive product of 2
# - most negative product of 2
# - highest product of 3
#
# For k, have to use DP - too many of these small variables to keep track of otherwise
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            max_product_of_k([-2,1,-3,4,-1,2,1,-5,4], 3), 60
        )

    def test_general_2(self):
        self.assertEqual(
            max_product_of_k([-2,1,-3,4,-1,2,1,-5,4], 5), 480
        )

if __name__ == '__main__':
    unittest.main()


