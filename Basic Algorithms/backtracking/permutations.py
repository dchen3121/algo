from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()  # optional

    def backtrack(sofar, used):
        if len(sofar) == len(nums):
            result.append(sofar.copy())
        else:
            for num in nums:
                if num not in used:
                    sofar.append(num)
                    used.add(num)
                    backtrack(sofar, used)
                    used.remove(num)
                    sofar.pop()

    backtrack([], set())
    return result


def permutations_w_dup(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()  # REQUIRED - makes sure all same nums are together. we only use a num if no same num before it has been used to avoid dups

    def backtrack(sofar, used):
        if len(sofar) == len(nums):
            result.append(sofar.copy())
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and used[i - 1]):
                    continue
                sofar.append(nums[i])
                used[i] = True
                backtrack(sofar, used)
                used[i] = False
                sofar.pop()

    backtrack([], [False for _ in range(len(nums))])
    return result

print(permutations_w_dup([1, 1, 2, 3]))
