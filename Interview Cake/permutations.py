# Write a recursive function for generating all permutations of an input string. Return them as a set.


from typing import Set


def permutations(s: str) -> Set:
    result = set()

    def permutations_help(sofar, index):
        if index == len(s):
            result.add(sofar)
            return
        for i in range(index + 1):
            permutations_help(sofar[:i] + s[index] + sofar[i:], index + 1)

    permutations_help('', 0)
    return result

print(permutations('abcd'))
