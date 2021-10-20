# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def canJumpFwd(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if max_reach >= len(nums) - 1:
                return True
            if i > max_reach:
                break
            max_reach = max(max_reach, i + nums[i])
        return max_reach >= len(nums) - 1

    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= pos:
                pos = i
        return not pos

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# 1. First idea is tree search, but we realize with tree search that certain indices will be visited multiple times
#    e.g. with [3, 2, 1, 0, 4], there is no need to check 2 and 1 since their max reach is the same as 3
# 2. Realizing this, we see if we can use dp so we avoid duplicate calculations. Idea is a dp array of length len(nums)
#    dp[i] is True if index i is reachable, and False otherwise
# 3. But we don't really need dp if all the information we need to track is a few indices - can just greedily go forward
# 4. Final improvement, don't necessarily need to check every index in forward pass, could just go backwards
# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# TESTING:
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

import unittest

class Test55(unittest.TestCase):

    def setUp(self):
        self.soln = Solution()

    def test_can(self):
        self.assertTrue(
            self.soln.canJump([2,3,1,1,4])
        )

    def test_cannot(self):
        self.assertFalse(
            self.soln.canJump([3,2,1,0,4])
        )

    def test_0(self):
        self.assertTrue(
            self.soln.canJump([0])
        )

if __name__ == '__main__':
    unittest.main()
