class Solution:
    
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item == '..' and stack:
                stack.pop()
            elif item != '' and item != '/':
                stack.append(item)
        return f'/{"/".join(stack)}'

