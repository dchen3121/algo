# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_y, max_x = len(grid), len(grid[0])

        for y in range(1, max_y):
            grid[y][0] += grid[y - 1][0]
        for x in range(1,  max_x):
            grid[0][x] += grid[0][x - 1]

        for y in range(1, max_y):
            for x in range(1, max_x):
                grid[y][x] += min(grid[y - 1][x], grid[y][x - 1])

        return grid[-1][-1]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# DP with more difficult input
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test64(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertAlmostEqual(
            self.soln.minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7
        )

    def test_general_2(self):
        self.assertAlmostEqual(
            self.soln.minPathSum([[1,2,3],[4,5,6]]), 12
        )

if __name__ == '__main__':
    unittest.main()
