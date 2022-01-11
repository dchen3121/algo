# Write a function for reversing a linked list. Do it in place.

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None

    def __repr__(self) -> str:
        result = [str(self.value)]
        node = self.next
        while node:
            result.append(str(node.value))
            node = node.next
        return ' -> '.join(result)


def reverse_linked_list(node: LinkedListNode) -> LinkedListNode:
    if not node or not node.next:
        return node
    result = LinkedListNode(0)
    result.next = node
    while node.next:
        tmp_node_next = node.next
        tmp_result = result.next
        node.next = node.next.next
        result.next = tmp_node_next
        result.next.next = tmp_result
    return result.next


n1 = LinkedListNode(1)
n2 = LinkedListNode(2)
n3 = LinkedListNode(3)
n4 = LinkedListNode(4)
n5 = LinkedListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(n1)
print(reverse_linked_list(n1))
