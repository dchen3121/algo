# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
            if i < 0:
                return 0
        result = 0
        while i >= 0 and s[i] != ' ':
            result += 1
            i -= 1
        return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# Straightforward string processing
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test58(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_general(self):
        self.assertEqual(
            self.soln.lengthOfLastWord("Hello World"), 5
        )

    def test_spaces(self):
        self.assertEqual(
            self.soln.lengthOfLastWord("   fly me   to   the moon  "), 4
        )

    def test_general_2(self):
        self.assertEqual(
            self.soln.lengthOfLastWord("luffy is still joyboy"), 6
        )

if __name__ == '__main__':
    unittest.main()
