# QUESTION:
# wildcard matching. * = any number of any characer, ? = any singular character

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isMatchHelp(s, p, s_index, p_index):
            # print(f's: {s}, p: {p}, s_index: {s_index}, p_index: {p_index}')
            if p_index == len(p):
                return s_index == len(s)
            if s_index == len(s):
                while p_index < len(p):
                    if p[p_index] != '*':
                        return False
                    p_index += 1
                return True
            if p[p_index] == '*':
                while s_index <= len(s):
                    success = isMatchHelp(s, p, s_index, p_index + 1)
                    if success:
                        return True
                    s_index += 1
                return False
            elif p[p_index] == '?' or p[p_index] == s[s_index]:
                return isMatchHelp(s, p, s_index + 1, p_index + 1)
            return False
        return isMatchHelp(s, p, 0, 0)

# IDEA:
# tree expansion

soln = Solution()
print(soln.isMatch('acdcb', 'a*c?b'))
print(soln.isMatch('adceb', '*a*b'))
print(soln.isMatch('aa', '*'))
print(soln.isMatch('aa', 'a'))
print(soln.isMatch('cb', '?a'))
print(soln.isMatch('', '***'))
print(soln.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))
