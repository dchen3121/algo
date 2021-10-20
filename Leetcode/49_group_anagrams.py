# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            if sorted_s in di:
                di[sorted_s].append(s)
            else:
                di[sorted_s] = [s]
        return list(di.values())


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Anagrams -> look for strings with same characters with same number of them -> sort the string to get the key
# There is a more advanced idea without sorting, where each letter is assigned a prime number (e.g. a = 2, b = 3, c = 5, etc) and the key is mult together
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test49(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertCountEqual(
            self.soln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]),
            [["eat","tea","ate"],["tan","nat"],["bat"]]
        )

    def test_empty(self):
        self.assertEqual(
            self.soln.groupAnagrams([""]),
            [[""]]
        )

    def test_single(self):
        self.assertEqual(
            self.soln.groupAnagrams(["a"]),
            [["a"]]
        )

if __name__ == '__main__':
    unittest.main()
