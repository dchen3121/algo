from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index_di = {}
        for index, num in enumerate(nums):
            if num_to_index_di.get(target - num) is not None:
                return [num_to_index_di[target - num], index]
            num_to_index_di[num] = index
        return [-1, -1]
