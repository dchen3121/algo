# QUESTION:
# Find all permutations of a list of numbers

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permuteHelp(sofar, nums, used, result):
            if len(sofar) == len(nums):
                result.append(sofar.copy())
                return
            for num in nums:
                if num not in used:
                    sofar.append(num)
                    used.add(num)
                    permuteHelp(sofar, nums, used, result)
                    used.remove(num)
                    sofar.pop()
        result = []
        permuteHelp([], nums, set(), result)
        return result

# IDEA:
# backtracking
