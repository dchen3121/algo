# QUESTION:
# Given a string s, return the longest palindromic substring in s.

# e.g.
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        longest_length = 0
        longest_length_substr = ''
        for i in range(len(s) - 1):
            start, end, curr_length = i - 1, i + 1, 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                curr_length += 2
                start -= 1
                end += 1
            if curr_length > longest_length:
                longest_length_substr = s[start + 1:end]
                longest_length = curr_length

            if s[i] == s[i + 1]:
                start, end, curr_length = i - 1, i + 2, 2
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    curr_length += 2
                    start -= 1
                    end += 1
                if curr_length > longest_length:
                    longest_length_substr = s[start + 1:end]
                    longest_length = curr_length

        return longest_length_substr

soln = Solution()
print(soln.longestPalindrome('babad'))
print(soln.longestPalindrome('abbab'))
print(soln.longestPalindrome('cbbd'))
print(soln.longestPalindrome('ac'))
print(soln.longestPalindrome('a'))

# IDEA:
# to look for palindromes, expand outwards
