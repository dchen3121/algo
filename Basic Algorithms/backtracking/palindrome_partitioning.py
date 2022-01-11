# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.


from typing import List


def palindrome_partition(s: str) -> List[str]:
    result = []

    def is_palindrome(start_index, end_index):
        while start_index < end_index:
            if s[start_index] != s[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True

    def backtrack(sofar, index):
        if index == len(s):
            result.append(sofar.copy())
        else:
            for i in range(index, len(s)):
                if is_palindrome(index, i):
                    sofar.append(s[index:i+1])
                    backtrack(sofar, i + 1)
                    sofar.pop()

    backtrack([], 0)
    return result


print(palindrome_partition("aabbcb"))

