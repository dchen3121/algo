# QUESTION:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

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

soln = Solution()
print(soln.permute([1,2,3,4]))
