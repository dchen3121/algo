# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given two binary strings a and b, return their sum as a binary string.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_index, b_index, carry, result = len(a) - 1, len(b) - 1, 0, ''

        while a_index >= 0 or b_index >= 0:
            curr_sum = carry
            if a_index >= 0:
                curr_sum += int(a[a_index])
            if b_index >= 0:
                curr_sum += int(b[b_index])
            a_index -= 1
            b_index -= 1
            result += str(curr_sum % 2)
            carry = curr_sum // 2

        if carry:
            result += str(carry)
        return result[::-1]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# go from back to front
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test67(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertEqual(
            self.soln.addBinary('11', '1'), '100'
        )

    def test_carry(self):
        self.assertEqual(
            self.soln.addBinary('1010', '1011'), '10101'
        )

if __name__ == '__main__':
    unittest.main()
