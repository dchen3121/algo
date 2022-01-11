# Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack.
# get_max() should not remove the item.
# Your stacks will contain only integers.


class Stack(object):
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.max_stack = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
        if not self.max_stack or item > self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        if self.max_stack and self.items[-1] == self.max_stack[-1]:
            self.max_stack.pop()

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(3)
print(stack.get_max())
stack.pop()
print(stack.get_max())
stack.pop()
print(stack.get_max())
stack.pop()
print(stack.get_max())
stack.pop()
print(stack.get_max())
