# QUESTION:
# implement strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        hlen, nlen = len(haystack), len(needle)
        if nlen > hlen:
            return -1
        for i in range(hlen - nlen + 1):
            if haystack[i] == needle[0]:
                if all(haystack[i + j] == needle[j] for j in range(nlen)):
                    return i
        return -1

