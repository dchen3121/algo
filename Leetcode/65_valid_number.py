# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# A valid number can be split up into these components (in order):
# 1. A decimal number or an integer.
# 2. (Optional) An 'e' or 'E', followed by an integer.
#
# A decimal number can be split up into these components (in order):
# 1. (Optional) A sign character (either '+' or '-').
# 2. One of the following formats:
#    a. One or more digits, followed by a dot '.'.
#    b. One or more digits, followed by a dot '.', followed by one or more digits.
#    c. A dot '.', followed by one or more digits.
#
# An integer can be split up into these components (in order):
# 1. (Optional) A sign character (either '+' or '-').
# 2. One or more digits.
#
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
# while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
#
# Given a string s, return true if s is a valid number.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List
import re

class Solution:
    def isNumber(self, s: str) -> bool:
        def isDigits(s: str) -> bool:
            if not s:
                return False
            return all(s[i].isdigit() for i in range(len(s)))

        def isInteger(s: str) -> bool:
            if not s:
                return False
            if s[0] in {'+', '-'}:
                return isDigits(s[1:])
            else:
                return isDigits(s)

        def isDecimalOrInteger(s: str) -> bool:
            if not s:
                return False
            if s[0] == '.':
                return isDigits(s[1:])
            elif s[0] in {'+', '-'}:
                if len(s) == 1 or not (s[1].isdigit() or s[1] == '.'):
                    return False
                return isDecimalOrInteger(s[1:])
            elif s[0].isdigit():
                i = 0
                while i < len(s) and s[i].isdigit():
                    i += 1
                if i == len(s) or (i == len(s) - 1 and s[i] == '.'):
                    return True
                elif s[i] == '.':
                    return isDigits(s[i + 1:])
                else:
                    return False
            else:
                return False

        if not 'e' in s and not 'E' in s:
            return isDecimalOrInteger(s)
        s = re.split('e|E', s)
        if len(s) != 2:
            return False
        return isDecimalOrInteger(s[0]) and isInteger(s[1])

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# string processing
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test65(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_valid(self):
        self.assertTrue(self.soln.isNumber("2"))
        self.assertTrue(self.soln.isNumber("0089"))
        self.assertTrue(self.soln.isNumber("-0.1"))
        self.assertTrue(self.soln.isNumber("+3.14"))
        self.assertTrue(self.soln.isNumber("4."))
        self.assertTrue(self.soln.isNumber("-.9"))
        self.assertTrue(self.soln.isNumber("2e10"))
        self.assertTrue(self.soln.isNumber("-90E3"))
        self.assertTrue(self.soln.isNumber("3e+7"))
        self.assertTrue(self.soln.isNumber("+6e-1"))
        self.assertTrue(self.soln.isNumber("53.5e93"))
        self.assertTrue(self.soln.isNumber("-123.45e6789"))

    def test_invalid(self):
        self.assertFalse(self.soln.isNumber("abc"))
        self.assertFalse(self.soln.isNumber("1a"))
        self.assertFalse(self.soln.isNumber("1e"))
        self.assertFalse(self.soln.isNumber("."))
        self.assertFalse(self.soln.isNumber("e3"))
        self.assertFalse(self.soln.isNumber("99e2.5"))
        self.assertFalse(self.soln.isNumber("--6"))
        self.assertFalse(self.soln.isNumber("-+3"))
        self.assertFalse(self.soln.isNumber("95a54e53"))

if __name__ == '__main__':
    unittest.main()
