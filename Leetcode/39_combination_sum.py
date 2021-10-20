# QUESION:
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationSumHelp(candidates, curr_candidates, index, left, result):
            if left == 0:
                result.append(curr_candidates.copy())
                return
            if left < candidates[index]:
                return
            for i in range(index, len(candidates)):
                curr_candidates.append(candidates[i])
                combinationSumHelp(candidates, curr_candidates, i, left - candidates[i], result)
                curr_candidates.pop()

        candidates.sort()
        result = []
        combinationSumHelp(candidates, [], 0, target, result)
        return result

# IDEA:
# backtracking

soln = Solution()
print(soln.combinationSum([2, 3, 5], 8))
print(soln.combinationSum([2, 3, 5], 10))
print(soln.combinationSum([2, 3, 5], 12))
print(soln.combinationSum([2, 3, 5], 0))
print(soln.combinationSum([2, 3, 5], 1))
