# QUESTION:
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Also return the number of unique numbers.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        prev_num = None
        for i, num in enumerate(nums):
            if num != prev_num:
                nums[index] = num
                index += 1
                prev_num = num
        return index
