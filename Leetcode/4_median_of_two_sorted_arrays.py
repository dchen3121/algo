# QUESTION:
# Find the median of two sorted arrays of length m and n in O(log(m + n)) time.

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(nums):
            if len(nums) % 2 == 0:
                return (nums[len(nums) / 2 - 1] + nums[len(nums) / 2]) / 2
            return nums[len(nums) // 2]

        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)

        m, n = len(nums1), len(nums2)
        # make sure nums1 is the shorter array
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # perform binary search
        start1, end1 = 0, len(nums1)
        while start1 < end1:
            mid1 = (start1 + end1) // 2
            mid2 = (m + n) // 2 - mid1

# IDEA:
# log indicates binary search
