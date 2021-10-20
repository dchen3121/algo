# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid.
# Now consider if some obstacles are added to the grids. How many unique paths would there be?\
# An obstacle and space is marked as 1 and 0 respectively in the grid.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return 0

        max_y, max_x = len(obstacleGrid), len(obstacleGrid[0])

        for y in range(max_y):
            if obstacleGrid[y][0] == 1:
                for i in range(y, max_y):
                    obstacleGrid[i][0] = 0
                break
            obstacleGrid[y][0] = 1

        for x in range(1, max_x):
            if obstacleGrid[0][x] == 1:
                for i in range(x, max_x):
                    obstacleGrid[0][i] = 0
                break
            obstacleGrid[0][x] = 1

        for y in range(1, len(obstacleGrid)):
            for x in range(1, len(obstacleGrid[0])):
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                else:
                    obstacleGrid[y][x] = obstacleGrid[y - 1][x] + obstacleGrid[y][x - 1]

        return obstacleGrid[-1][-1]



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# DP with input processing
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test63(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertAlmostEqual(
            self.soln.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2
        )

    def test_general_2(self):
        self.assertAlmostEqual(
            self.soln.uniquePathsWithObstacles([[0,1],[0,0]]), 1
        )

if __name__ == '__main__':
    unittest.main()
