# QUESTION:
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start

# IDEA:
# binary search

soln = Solution()
print(soln.searchInsert([1,3,5,6,7,8,10,12], 1))
print(soln.searchInsert([1,3,5,6,7,8,10,12], 2))
print(soln.searchInsert([1,3,5,6,7,8,10,12], 4))
print(soln.searchInsert([1,3,5,6,7,8,10,12], 6))
print(soln.searchInsert([1,3,5,6,7,8,10,12], 8))
print(soln.searchInsert([1,3,5,6,7,8,10,12], 11))
print(soln.searchInsert([1,3,5,6,7,8,10,12], 12))
