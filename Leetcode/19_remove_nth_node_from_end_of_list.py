# QUESTION:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        result = ListNode(0, head)
        curr_start = curr_end = result
        for _ in range(n):
            curr_end = curr_end.next
        while curr_end.next:
            curr_start = curr_start.next
            curr_end = curr_end.next
        curr_start.next = curr_start.next.next
        return result.next
