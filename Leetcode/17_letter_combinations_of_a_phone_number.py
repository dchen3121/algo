# QUESTION:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_to_char_di = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        results = ['']

        for digit in digits:
            possible_chars = num_to_char_di[digit]
            new_results = []
            for result in results:
                for char in possible_chars:
                    new_results.append(result + char)
            results = new_results

        return results

# IDEA:
# can be done iteratively or recursively

soln = Solution()
print(soln.letterCombinations('2345'))

