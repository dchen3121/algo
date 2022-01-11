from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(sofar, index, target):
        if target == 0:
            result.append(sofar.copy())
        elif target < 0:
            return
        else:
            for i in range(index, len(candidates)):
                backtrack(sofar + [candidates[i]], i, target - candidates[i])

    backtrack([], 0, target)
    return result


def combination_sum_no_reuse(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def backtrack(sofar, index, target):
        if target == 0:
            result.append(sofar.copy())
        elif target < 0:
            return
        else:
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(sofar + [candidates[i]], i + 1, target - candidates[i])

    backtrack([], 0, target)
    return result


# print(combination_sum_no_reuse([5,3,2], 8))
# print(combination_sum_no_reuse([1,2,3,5,6,7], 9))
print(combination_sum_no_reuse([10,1,2,7,6,1,5,1], 8))
