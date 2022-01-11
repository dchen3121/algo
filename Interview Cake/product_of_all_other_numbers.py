# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# Here's the catch: You can't use division in your solution!

# Example:
# input: [1, 7, 3, 4]
# output: [84, 12, 28, 21] ( [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3] )


from typing import List


def get_products_of_all_ints_except_at_index(nums: List[int]) -> List[int]:
    product_before = [1 for _ in range(len(nums))]
    product_after = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        product_before[i] = product_before[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        product_after[i] = product_after[i + 1] * nums[i + 1]

    return [product_before[i] * product_after[i] for i in range(len(nums))]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# DP
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            get_products_of_all_ints_except_at_index([1, 7, 3, 4]), [84, 12, 28, 21]
        )

if __name__ == '__main__':
    unittest.main()


# REVIEW FOR LATER!
