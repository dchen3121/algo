# QUESTION:
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            raise Exception('ERROR: invalid input')

        nums.sort()
        closest_range = abs(target - nums[0] - nums[1] - nums[2])
        closest_value = nums[0] + nums[1] + nums[2]

        for i, curr_num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = curr_num + nums[left] + nums[right]
                if curr_sum == target:
                    return target
                if abs(curr_sum - target) < closest_range:
                    closest_value = curr_sum
                    closest_range = min(abs(curr_sum - target), closest_range)

                if curr_sum - target > 0:
                    right -= 1
                    while right > left and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return closest_value

# IDEA:
# see 15. 3 sum

soln = Solution()
print(soln.threeSumClosest([-1,2,1,4], 1))
