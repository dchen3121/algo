# QUESTION:
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_height = 0, len(height) - 1, 0
        while left < right:
            if height[left] < height[right]:
                max_height = max(max_height, height[left] * (right - left))
                left += 1
            else:
                max_height = max(max_height, height[right] * (right - left))
                right -= 1
        return max_height

# IDEA:
# the greedy 2ptr classic

soln = Solution()
print(soln.maxArea([1,8,6,2,5,4,8,3,7]))
print(soln.maxArea([1,2]))
print(soln.maxArea([4,3,2,1,4]))
print(soln.maxArea([1,2,1]))
