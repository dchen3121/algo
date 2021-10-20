# QUESTION:
# given a number, find th next biggest permutation of the number

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_decreasing_index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                first_decreasing_index = i - 1
                break

        if first_decreasing_index == -1:
            nums.reverse()
            return nums

        if first_decreasing_index == len(nums) - 2:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return nums

        min_num_greater_than_first_decreasing_index = None
        for i in range(len(nums) - 1, first_decreasing_index, -1):
            if (min_num_greater_than_first_decreasing_index is None or nums[i] < nums[min_num_greater_than_first_decreasing_index]) and nums[i] > nums[first_decreasing_index]:
                min_num_greater_than_first_decreasing_index = i

        nums[first_decreasing_index], nums[min_num_greater_than_first_decreasing_index] = nums[min_num_greater_than_first_decreasing_index], nums[first_decreasing_index]

        def reverse_list_between_indices(list, left, right):
            while right > left:
                list[left], list[right] = list[right], list[left]
                right -= 1
                left += 1

        reverse_list_between_indices(nums, first_decreasing_index + 1, len(nums) - 1)

        return nums



# IDEA:
# the algorithm:
# go reverse from end to start of nums. find first decreasing pair.
# for the left of the pair, find the smallest elem in the right that's bigger than it. if there are multiple, take the rightermost one.
# swap the two.
# after swap, reverse the right side.

soln = Solution()
print(soln.nextPermutation([1,2,3]))
print(soln.nextPermutation([1,3,2]))
print(soln.nextPermutation([2,1,3]))
print(soln.nextPermutation([2,3,1]))
print(soln.nextPermutation([3,1,2]))
print(soln.nextPermutation([3,2,1]))
print(soln.nextPermutation([2,3,1,3,3,3]))
