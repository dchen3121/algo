# QUESTION:
# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        while index < len(strs[0]):
            curr_char = strs[0][index]
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or strs[i][index] != curr_char:
                    return strs[0][:index]
            index += 1
        return strs[0]

# IDEA:
# horizontal scanning

soln = Solution()
print(soln.longestCommonPrefix(["flower","flow","flight"]))
print(soln.longestCommonPrefix(["flow","flower","flight"]))
print(soln.longestCommonPrefix(["dog","racecar","car"]))
