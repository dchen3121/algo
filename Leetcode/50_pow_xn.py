# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def oldPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = n < 0
        n = abs(n)

        result = 1
        while n > 0:
            result *= x
            n -= 1

        if neg:
            return 1 / result
        return result

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        if n % 2 == 0:
            return self.myPow(self.myPow(x, n // 2), 2)
        else:
            return x * self.myPow(self.myPow(x, n // 2), 2)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Naive solution works for small numbers, but fail at large
# Can break down into cases for a recursive solution. Top down over bottom up!
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test50(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertAlmostEqual(
            self.soln.myPow(2, 10), 1024
        )

    def test_fp(self):
        self.assertAlmostEqual(
            self.soln.myPow(2.10000, 3), 9.261
        )

    def test_neg_expt(self):
        self.assertAlmostEqual(
            self.soln.myPow(2.00000, -2), 0.25
        )

if __name__ == '__main__':
    unittest.main()
