from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def backtrack(sofar, index):
        result.append(sofar.copy())
        for i in range(index, len(nums)):
            backtrack(sofar + [nums[i]], i + 1)

    backtrack([], 0)
    return result


def subsets_w_dup(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def backtrack(sofar, index):
        result.append(sofar.copy())
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            backtrack(sofar + [nums[i]], i + 1)

    backtrack([], 0)
    return result


print(subsets([1, 1, 2]))
print(subsets_w_dup([1, 1, 2]))

