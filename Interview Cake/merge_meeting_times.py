# Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
# To do this, you’ll need to know when any team is having a meeting.
# In HiCal, a meeting is stored as a tuple of integers (start_time, end_time).
# Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
# Do not assume the meetings are in order. The meeting times are coming from multiple teams.

# Example:
# input: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# output: [(0, 1), (3, 8), (9, 12)]


from typing import List, Tuple


def merge_meeting_times(meeting_times: List[Tuple]) -> List[Tuple]:
    if len(meeting_times) <= 1:
        return meeting_times

    meeting_times.sort(key=lambda x: x[0])
    result = [meeting_times[0]]

    for _, meeting_time in enumerate(meeting_times):
        start_time, end_time = meeting_time
        if start_time <= result[-1][1]:
            start_time, _ = result.pop()
        result.append((start_time, end_time))

    return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Sorting the list makes a greedy approach possible. O(n log n) where n is length of list.
#
# We started off trying to solve the problem in one pass, and we noticed that it wouldn't work.
# We then noticed the reason it wouldn't work: to see if a given meeting can be merged, we have to look at all the other meetings!
# That's because the order of the meetings is random.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            merge_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]),
            [(0, 1), (3, 8), (9, 12)]
        )

if __name__ == '__main__':
    unittest.main()
