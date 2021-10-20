# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTION:
# Given the head of a linked list, rotate the list to the right by k places.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        k %= length
        if k == 0:
            return head
        k = length - k
        curr = ListNode(0, head)
        for _ in range(k):
            curr = curr.next
        result = curr.next
        curr.next = None
        curr = result
        while curr.next:
            curr = curr.next
        curr.next = head
        return result


# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# IDEA:
# either 1 pass with 2 ptrs or 2 pass is the same
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# for some reason my linked list solutions are always messy af, need to work on this
