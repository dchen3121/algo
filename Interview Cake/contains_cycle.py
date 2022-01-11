# Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None


def contains_cycle_old(node: LinkedListNode) -> bool:
    visited = set()
    while node:
        if node in visited:
            return False
        visited.add(node)
        node = node.next
    return True


# tortoise and hare
def contains_cycle(first_node):
    # Start both runners at the beginning
    slow_runner = first_node
    fast_runner = first_node

    # Until we hit the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # Case: fast_runner is about to "lap" slow_runner
        if fast_runner is slow_runner:
            return True

    # Case: fast_runner hit the end of the list
    return False

