# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_start, curr_end, prev_end = intervals[i][0], intervals[i][1], result[-1][1]
            if curr_start <= prev_end:
                result[-1][1] = max(prev_end, curr_end)
            else:
                result.append([curr_start, curr_end])
        return result

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Can't handle the input efficiently as is, sorting by start time leads to the best results
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test56(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertEqual(
            self.soln.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]]
        )

    def test_overlap(self):
        self.assertEqual(
            self.soln.merge([[1,4],[4,5]]), [[1,5]]
        )

if __name__ == '__main__':
    unittest.main()
