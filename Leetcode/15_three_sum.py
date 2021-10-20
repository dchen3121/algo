# QUESTION:
# 3-sum.
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            curr_num = nums[i]
            if curr_num > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = curr_num + nums[left] + nums[right]
                if curr_sum == 0:
                    result.append([curr_num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    right -= 1
                    while right > left and nums[right + 1] == nums[right]:
                        right -= 1
                elif curr_sum > 0:
                    right -= 1
                    while right > left and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return result

# IDEA:
# brute force -> find all possible triplets, O(n^3) time.
# with sorting, we can potentially get rid of duplicate work.
# key: two pointers

soln = Solution()
print(soln.threeSum([-1,0,1,2,-1,-4]))
print(soln.threeSum([]))
print(soln.threeSum([0]))
print(soln.threeSum([-2,0,1,1,2]))
