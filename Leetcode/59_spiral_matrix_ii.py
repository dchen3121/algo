# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[None for _ in range(n)] for _ in range(n)]
        x, y, left, right, top, bottom, direction = 0, 0, 0, n - 1, 0, n - 1, '>'
        for i in range(1, n * n + 1):
            result[y][x] = i
            if direction == '>':
                if x >= right:
                    direction = 'v'
                    top += 1
                    y += 1
                else:
                    x += 1
            elif direction == 'v':
                if y >= bottom:
                    direction = '<'
                    right -= 1
                    x -= 1
                else:
                    y += 1
            elif direction == '<':
                if x <= left:
                    direction = '^'
                    bottom -= 1
                    y -= 1
                else:
                    x -= 1
            elif direction == '^':
                if y <= top:
                    direction = '>'
                    left += 1
                    x += 1
                else:
                    y -= 1
        return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Keep wall trackers and go in a spiral
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test59(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertEqual(
            self.soln.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]]
        )

    def test_1(self):
        self.assertEqual(
            self.soln.generateMatrix(1), [[1]]
        )

if __name__ == '__main__':
    unittest.main()
