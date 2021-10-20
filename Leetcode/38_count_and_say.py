# QUESTION:
# Given a positive integer n, return the nth term of the count-and-say sequence, starting with '1'

class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            next_result = []
            curr_num, curr_len = result[0], 0
            for num in result:
                if num == curr_num:
                    curr_len += 1
                else:
                    next_result.append(f'{curr_len}{curr_num}')
                    curr_num = num
                    curr_len = 1
            next_result.append(f'{curr_len}{curr_num}')
            result = ''.join(next_result)
        return result

soln = Solution()
print(soln.countAndSay(6))
