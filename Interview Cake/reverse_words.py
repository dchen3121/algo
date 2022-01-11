# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault.
# The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.
# Write a function reverse_words()which takes a message as a list of characters, then reverses the order of the words in place.

# Example:
# input: ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
# output: ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e']


from typing import List


def reverse_words(letters: List[str]) -> None:
    def reverse_word(start, end):
        # takes start and end indices and swaps every char in between, inclusive.
        while start < end:
            letters[start], letters[end] = letters[end], letters[start]
            start += 1
            end -= 1

    start = 0
    while start < len(letters):
        while letters[start] == ' ':
            start += 1
        end = start
        while end < len(letters) and letters[end] != ' ':
            end += 1
        reverse_word(start, end - 1)
        start = end

    reverse_word(0, len(letters) - 1)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# First, notice that if we tried to swap each word individually it would take too long.
# Then, realize that we can first flip each word then flip the whole sentence.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):

    def test_general(self):
        test_list = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
        reverse_words(test_list)
        self.assertEqual(
            test_list, ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e']
        )

if __name__ == '__main__':
    unittest.main()
