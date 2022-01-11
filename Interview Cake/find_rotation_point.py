# Write a function for finding the index of the "rotation point" for words from a dictionary.
# This list is huge so we want to be efficient here.

# Example:
# input: [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]
# output: 5


from typing import List


def find_rotation_point(words: List[str]) -> int:
    if len(words) <= 1:
        return 0

    start, end = 0, len(words) - 1

    while start <= end:
        if start == end:
            return start
        if start + 1 == end:
            # ['a', 'b']
            # ['b', 'a']
            return start if words[start] < words[end] else end

        mid = (start + end) // 2
        if words[mid] > words[start]:
            # two cases
            if words[mid] < words[end]:
                # ['a', 'b', 'c', 'd', 'e']
                end = mid
            else:
                # ['c', 'd', 'e', 'a', 'b']
                start = mid
        else:
            # ['f', 'g', 'a', 'b', 'c', 'd', 'e']
            end = mid

    return -1



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# binary search with a twist - still O(log n)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        words = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here
            'babka',
            'banoffee',
            'banz',
            'endanger',
            'engender',
            'karpatka',
            'othellolagkage',
        ]
        self.assertEqual(
            find_rotation_point(words), 5
        )

    def test_unrotated(self):
        words = [
            'asymptote',  # <-- rotates here
            'babka',
            'banoffee',
            'banz',
            'endanger',
            'engender',
            'karpatka',
            'othellolagkage',
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
        ]
        self.assertEqual(
            find_rotation_point(words), 0
        )

if __name__ == '__main__':
    unittest.main()


# REVIEW FOR LATER!
