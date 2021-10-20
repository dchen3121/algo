# QUESTION:
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements CAN be changed. It doesn't matter what you leave beyond the new length.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while right > left and nums[right] == val:
            right -= 1
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                while right > left and nums[right] == val:
                    right -= 1
            left += 1
        while left < len(nums) and nums[left] != val:
            left += 1
        return left


soln = Solution()
print(soln.removeElement([0,1,2,4,3,2,2,4,2,1,0], 2))
print(soln.removeElement([3,2,2,3,2,2,2], 3))
print(soln.removeElement([], 3))
