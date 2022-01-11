# Let's say:

# - '(', '{', '[' are called "openers"
# - ')', '}', ']' are called "closers"

# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

# Examples:

# - "{ ( ) }" should return True
# - "{ [ ( ] ) }" should return False
# - "{ [ }" should return False


def valid_parentheses(parens: str) -> bool:
    di = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = []
    for paren in parens:
        if paren in di:
            if not stack or stack[-1] != di[paren]:
                return False
            stack.pop()
        else:
            stack.append(paren)

    return not stack
