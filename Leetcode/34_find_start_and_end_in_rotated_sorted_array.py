# QUESTION:
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start_index, end_index = mid, mid
                while start_index > 0 and nums[start_index - 1] == nums[mid]:
                    start_index -= 1
                while end_index < len(nums) - 1 and nums[end_index + 1] == nums[mid]:
                    end_index += 1
                return [start_index, end_index]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]

# IDEA:
# O(log n) complexity immediately indicates binary search.
# Perform binary search on the number index then expand on it

soln = Solution()
print(soln.searchRange([1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10], 1))
print(soln.searchRange([1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10], 4))
print(soln.searchRange([1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10], 7))
print(soln.searchRange([1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10], 9))
print(soln.searchRange([1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10], 10))
print(soln.searchRange([1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10], 0))
print(soln.searchRange([], 0))
