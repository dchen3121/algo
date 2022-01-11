# Write an efficient function that checks whether any permutation of an input string is a palindrome.

# Examples:
# "civic" -> True
# "ivicc" -> True
# "iiivc" -> False


def has_palindrome_permutation(s: str) -> bool:
    char_set = set()

    for char in s:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)

    return len(char_set) <= 1


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# a string is a permutation of a palindrome if all (or all but one) of its character count is even. just go through the string. O(n) where n = len(s)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        self.assertEqual(
            has_palindrome_permutation("ivicc"), True
        )

    def test_general_2(self):
        self.assertEqual(
            has_palindrome_permutation("ciiiv"), False
        )

if __name__ == '__main__':
    unittest.main()
