# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given an m x n matrix, return all elements of the matrix in spiral order.
# e.g.
#   Input:  [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [1,2,3,6,9,8,7,4,5]
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        left, right, top, bot = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        curr_x, curr_y, dir = 0, 0, '>'  # dir is one of {'<', '>', '^', 'v'}
        result = []
        while left <= right and top <= bot:
            result.append(matrix[curr_y][curr_x])
            if dir == '>':
                if curr_x < right:
                    curr_x += 1
                else:
                    dir = 'v'
                    top += 1
                    curr_y += 1
            elif dir == 'v':
                if curr_y < bot:
                    curr_y += 1
                else:
                    dir = '<'
                    right -= 1
                    curr_x -= 1
            elif dir == '<':
                if curr_x > left:
                    curr_x -= 1
                else:
                    dir = '^'
                    bot -= 1
                    curr_y -= 1
            elif dir == '^':
                if curr_y > top:
                    curr_y -= 1
                else:
                    dir = '>'
                    left += 1
                    curr_x += 1
        return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Only one way to really do it - setting boundaries to loop around the whole matrix
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test54(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_3x3(self):
        self.assertAlmostEqual(
            self.soln.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5]
        )

    def test_4x4(self):
        self.assertAlmostEqual(
            self.soln.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7]
        )

if __name__ == '__main__':
    unittest.main()
