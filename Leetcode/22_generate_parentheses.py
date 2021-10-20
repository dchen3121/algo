# QUESTION:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# e.g. n = 3, answer: ["((()))","(()())","(())()","()(())","()()()"]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def genRec(curr, num_left, num_right, result):
            if num_right == 0:
                result.append(curr)
                return
            if num_left > 0:
                genRec(curr + '(', num_left - 1, num_right, result)
            if num_right > num_left:
                genRec(curr + ')', num_left, num_right - 1, result)
        result = []
        genRec('', n, n, result)
        return result

# IDEA:
# can only have more left than right

soln = Solution()
print(soln.generateParenthesis(4))
print(soln.generateParenthesis(0))
print(soln.generateParenthesis(9))
