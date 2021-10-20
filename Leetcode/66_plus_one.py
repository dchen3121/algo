# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            if i == 0:
                return [1] + digits
            i -= 1
            digits[i] += 1
        return digits


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# go from back to front
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test66(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertAlmostEqual(
            self.soln.plusOne([1,2,3]), [1,2,4]
        )

    def test_carry(self):
        self.assertAlmostEqual(
            self.soln.plusOne([9,9,9]), [1,0,0,0]
        )

if __name__ == '__main__':
    unittest.main()
