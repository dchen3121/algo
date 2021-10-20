# QUESTION:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_di = {']': '[', '}': '{', ')': '('}
        stack = []
        for bracket in s:
            if bracket in brackets_di:
                if not stack or brackets_di[bracket] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return not stack

soln = Solution()
print(soln.isValid('()[]{}'))
print(soln.isValid('()[}{]'))
print(soln.isValid('()[{]}'))
print(soln.isValid('}'))
print(soln.isValid('}'))
print(soln.isValid(''))
