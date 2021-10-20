# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[-1][-1]



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Intro level dp
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test62(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertAlmostEqual(
            self.soln.uniquePaths(3, 7), 28
        )

    def test_general_2(self):
        self.assertAlmostEqual(
            self.soln.uniquePaths(3, 3), 6
        )

if __name__ == '__main__':
    unittest.main()
