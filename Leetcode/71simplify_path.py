class Solution:

    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item == '..':
                if stack: 
                    stack.pop()
            elif item != '' and item != '.':
                stack.append(item)
        return f'/{"/".join(stack)}'

# Difficulty: medium
# Key point: think how the directory structure is just like a stack
