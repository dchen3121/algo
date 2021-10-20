# QUESTION:
# Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        y = 0
        while y < x:
            y *= 10
            y += x % 10
            x //= 10
        return y == x or y // 10 == x

# IDEA:
# converting to string is easy
# if staying numerical, trick is to divide in half until the latter half is longer than the first half, then check if the two are opposite

soln = Solution()
print(soln.isPalindrome(1234321))
print(soln.isPalindrome(12323))
print(soln.isPalindrome(1232321))
print(soln.isPalindrome(123321))
print(soln.isPalindrome(1))
print(soln.isPalindrome(10))
print(soln.isPalindrome(-123321))
