# QUESTION:
# Given an unsorted integer array nums, find the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                nums[i] = 0
        for i in range(len(nums)):
            curr_num = nums[i]
            while curr_num != 0 and i != curr_num - 1:
                nums[i], nums[curr_num - 1] = nums[curr_num - 1], nums[i]
                if nums[i] == nums[curr_num - 1]:
                    nums[i] = 0
                else:
                    curr_num = nums[i]
        for i, num in enumerate(nums):
            if num == 0:
                return i + 1
        return len(nums) + 1

# IDEA: use the indices of the array nums as additional information that we can use.

soln = Solution()
print(soln.firstMissingPositive([3,4,-1,1]))
print(soln.firstMissingPositive([3,2,-1,1]))
print(soln.firstMissingPositive([7,8,9,11,12]))
print(soln.firstMissingPositive([1]))
print(soln.firstMissingPositive([-1]))
