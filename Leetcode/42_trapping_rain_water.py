# QUESTION:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List

class OldSolution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right, max_left_arr, max_right_arr = 0, 0, [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        for i in range(len(height)):
            if height[i] > max_left:
                max_left = height[i]
            max_left_arr[i] = max_left
        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_right:
                max_right = height[i]
            max_right_arr[i] = max_right

        result = 0
        for i in range(len(height)):
            result += min(max_left_arr[i], max_right_arr[i]) - height[i]
        return result

# FIRST IDEA:
# DP. Assume tall wall on left and right to begin with.
# e.g. if tall wall on right, then at each step we just need to add max height of left - curr height
# at the end, take min.

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        max_left, max_right, left, right, result = height[0], height[-1], 0, len(height) - 1, 0
        while left < right:
            if max_left < max_right:
                result += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                result += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        return result

# SECOND IDEA:
# 2 ptrs. From DP solution we can see that tracking so much info is not needed.

soln = Solution()
print(soln.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(soln.trap([4,2,0,3,2,5])) # 9
