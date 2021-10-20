# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# 1. "123"
# 2. "132"
# 3. "213"
# 4. "231"
# 5. "312"
# 6. "321"
# Given n and k, return the kth permutation sequence.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# n = 3, n! = 6, (n - 1)! = 2, k = 3 - 1 = 2
#   k // (n - 1)! = 2 // 2 = 1
#   k % (n - 1)! = 2 % 2 = 0
#   in index 1 (2), 0 remaining, join 13, ans: 213
# n = 4, n! = 24, (n - 1)! = 6, k = 9 - 1 = 8
#   k // (n - 1)! = 8 // 6 = 1
#   k % (n - 1)! = 2
#   in index 1 (2), 2 remaining, new k = 2, decrease n by 1
#   k // (n - 1)! = 2 // 2! = 1
#   k % (n - 1)! = 0
#   in index 1 (3), 0 remaining, join 14, ans: 2314

from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n + 1)]
        result = ''

        k -= 1
        while n > 1 and k != 0:
            section, k = divmod(k, factorial(n - 1))
            result += str(numbers[section])
            del numbers[section]
            n -= 1

        result += ''.join([str(num) for num in numbers])
        return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Total of n! permutations.
# The first (n - 1) starts with 1, the next (n - 1) starts with 2, ..., the last (n - 1) starts with n
# Continue on with the pattern.
# k -= 1 is key!
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test60(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertEqual(
            self.soln.getPermutation(3,3), '213'
        )

    def test_general_2(self):
        self.assertEqual(
            self.soln.getPermutation(4,9), '2314'
        )

    def test_general_3(self):
        self.assertEqual(
            self.soln.getPermutation(4,10), '2341'
        )

if __name__ == '__main__':
    unittest.main()
