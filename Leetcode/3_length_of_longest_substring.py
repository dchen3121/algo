class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_di = {}
        substring_start_index = 0
        longest_substring_length = 0

        for i, c in enumerate(s):
            if c in char_index_di and char_index_di[c] >= substring_start_index:
                longest_substring_length = max(longest_substring_length, i - substring_start_index)
                substring_start_index = char_index_di[c] + 1
            char_index_di[c] = i

        return max(longest_substring_length, len(s) - substring_start_index)

soln = Solution()
print(soln.lengthOfLongestSubstring('babad'))
print(soln.lengthOfLongestSubstring('abbab'))
print(soln.lengthOfLongestSubstring('cbbd'))
print(soln.lengthOfLongestSubstring('ac'))
print(soln.lengthOfLongestSubstring('a'))

# IDEA:
# greedy
