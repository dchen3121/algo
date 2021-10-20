from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # perform binary search
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if nums[mid] < nums[start]:
                    # [6, 7, 8, 0, 1, 2, 3, 4, 5]
                    end = mid - 1
                else:
                    # [3, 4, 5, 6, 7, 8, 0, 1, 2]
                    if target >= nums[start]:
                        end = mid - 1
                    else:
                        start = mid + 1
            else:
                if nums[mid] < nums[start]:
                    # [6, 7, 8, 0, 1, 2, 3, 4, 5]
                    if target >= nums[start]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    # [3, 4, 5, 6, 7, 8, 0, 1, 2]
                    start = mid + 1
        return -1

    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

soln = Solution()
print(soln.search([4,5,6,7,0,1,2], 4))
print(soln.search([4,5,6,7,0,1,2], 0))
print(soln.search([4,5,6,7,0,1,2], 3))
print(soln.search([4,5,6,7,0,1,2], 2))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
# print(soln.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))
