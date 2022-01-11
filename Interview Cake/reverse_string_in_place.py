# Write a function that takes a list of characters and reverses the letters in place.

# Example:
# input: ['a', 'b', 'c']
# output: ['c', 'b', 'a']


from typing import List


def reverse_letters(letters: List[str]) -> None:
    for i in range(len(letters) // 2):
        letters[i], letters[-(i + 1)] = letters[-(i + 1)], letters[i]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# To do this in place, we just have to perform swaps.
# We only need to swap half the list.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        test_list = ['a', 'b', 'c']
        reverse_letters(test_list)
        self.assertEqual(
            test_list, ['c', 'b', 'a']
        )

if __name__ == '__main__':
    unittest.main()
