# Build a queue with two stacks

class Queue:
    def __init__(self) -> None:
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, value) -> None:
        self.stack_1.append(value)

    def dequeue(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
