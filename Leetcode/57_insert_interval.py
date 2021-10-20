# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent the start and the end of
# the i-th interval and intervals are sorted in ascending order by start_i. You are also given an interval newInterval = [start, end]
# that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals are still sorted in ascending order by start_i and intervals still do not have any
# overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        new_start, new_end = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            if interval[1] < new_start:
                left.append(interval)
            elif interval[0] > new_end:
                right.append(interval)
            else:
                new_start = min(new_start, interval[0])
                new_end = max(new_end, interval[1])

        return left + [[new_start, new_end]] + right



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Find left, find right, deal with middle. Note that in this particular algo it doesn't really matter if sorted
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test57(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertEqual(
            self.soln.insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]]
        )

    def test_overlap_more_than_1(self):
        self.assertEqual(
            self.soln.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]]
        )

    def test_no_orig_intervals(self):
        self.assertEqual(
            self.soln.insert([], [1,2]), [[1,2]]
        )

if __name__ == '__main__':
    unittest.main()
