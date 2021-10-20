# QUESTION:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                num_i, num_j = nums[i], nums[j]
                start, end = j + 1, len(nums) - 1
                while start < end:
                    curr_sum = num_i + num_j + nums[start] + nums[end]
                    if curr_sum == target:
                        result.append([num_i, num_j, nums[start], nums[end]])
                        start += 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        end -= 1
                        while end > start and nums[end] == nums[end + 1]:
                            end -= 1
                    elif curr_sum < target:
                        start += 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                    else:
                        end -= 1
                        while end > start and nums[end] == nums[end + 1]:
                            end -= 1
        return result

# IDEA:
# see 3Sum. same idea, 2 pointers

soln = Solution()
print(soln.fourSum([1,0,-1,0,-2,2], 0))
print(soln.fourSum([2,2,2,2,2,2], 8))
