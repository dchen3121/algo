# QUESTION:
# You are given a string s and an array of strings words of the same length k.
# Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.

from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

# IDEA:
# first thought: check every possible substr and see if it is a concatenation of all once.
