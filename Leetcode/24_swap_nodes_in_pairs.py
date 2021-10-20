# QUESTION:
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode(0, head)
        curr = result
        while curr.next and curr.next.next:
            tmp3 = curr.next.next.next # tmp3 = 3 in [1, 2, 3, 4]
            tmp2 = curr.next.next      # tmp2 = 2 in [1, 2, 3, 4]
            curr.next.next = tmp3
            tmp2.next = curr.next
            curr.next = tmp2
            curr = curr.next.next
        return result.next
