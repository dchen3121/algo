# QUESTION:
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# O(n^2) approach
class OldSolution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        current_indices = set() # the indices we are currently still checking
        info = []
        for i, paren in enumerate(s):
            if paren == '(':
                info.append({'num-lefts': 0, 'longest-starting-here': 0, 'curr-length': 0})
                current_indices.add(i)
                for index in current_indices:
                    info[index]['num-lefts'] += 1
                    info[index]['curr-length'] += 1
            else:
                info.append({'num-lefts': 0, 'longest-starting-here': 0, 'curr-length': 0})
                to_remove = set()
                for index in current_indices:
                    if info[index]['num-lefts'] == 0:
                        to_remove.add(index)
                    else:
                        info[index]['num-lefts'] -= 1
                        info[index]['curr-length'] += 1
                        if info[index]['num-lefts'] == 0:
                            info[index]['longest-starting-here'] = info[index]['curr-length']
                for index in to_remove:
                    current_indices.remove(index)
        return max(info, key=lambda x: x['longest-starting-here'])['longest-starting-here']

# IDEA 1:
# first approach that comes to mind:
# would have to greedily expand on every paren and check where longest valid ends
# what do we need to keep track of?
    # for each index: number of left-brackets, current longest length of complete parens starting from that index, current length, and if it still needs to be checked
# worst case O(n^2) - this seems like it exceeds time limit.
# can we do this in O(n)?

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        max_ending_here = [0 for _ in range(len(s))]
        max_result = 0

        left_bracket_locations = []

        for i, paren in enumerate(s):
            if paren == '(':
                left_bracket_locations.append(i)
            else:
                if left_bracket_locations:
                    last_left_bracket_location = left_bracket_locations.pop()
                    max_ending_here[i] = i - last_left_bracket_location + 1
                    if last_left_bracket_location > 0:
                        max_ending_here[i] += max_ending_here[last_left_bracket_location - 1]
                    max_result = max(max_ending_here[i], max_result)
        return max_result

# IDEA 2:
# to try to do this in O(n), we would have to store more info in the DP array.
# at each index in the array, we can store:
    # the max possible number of left-brackets, max result ending with parens ending at that index
# also store the locations of all left brackets
# if the current location is a right-bracket, it would check where the last left bracket is, and set max ending here to curr_index - last_left_bracket_index and remove last left bracket from list
# now O(n)!

soln = Solution()
print(soln.longestValidParentheses(')(())()())'))
print(soln.longestValidParentheses(')()'))
print(soln.longestValidParentheses(')()())'))
print(soln.longestValidParentheses(')'))
print(soln.longestValidParentheses('('))
print(soln.longestValidParentheses(''))
