# QUESTION:
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        start, end = 0, 0
        while end < len(nums) - 1:
            num_jumps += 1
            max_end = end
            for i in range(start, end + 1):
                max_end = max(max_end, nums[i] + i)
                if max_end > len(nums) - 1:
                    return num_jumps
            start = end + 1
            end = max_end
        return num_jumps

# IDEA:
# greedy
