# QUESTION:
# Given a collection of possibly duplicate candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationSum2Help(candidates, sofar, index, left, result):
            if left == 0:
                result.append(sofar.copy())
                return
            if index == len(candidates) or left < candidates[index]:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                sofar.append(candidates[i])
                combinationSum2Help(candidates, sofar, i + 1, left - candidates[i], result)
                sofar.pop()

        candidates.sort()
        result = []
        combinationSum2Help(candidates, [], 0, target, result)
        return result

# IDEA:
# again, backtracking

soln = Solution()
print(soln.combinationSum2([10,1,2,7,6,1,5], 8))
print(soln.combinationSum2([10,1,2,7,6,1,5], 1))
print(soln.combinationSum2([10,1,2,7,6,1,5], 2))
print(soln.combinationSum2([10,1,2,7,6,1,5], 100))