# QUESTION:
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseK(head, k):
            test = ListNode(0, head)
            for _ in range(k):
                test = test.next
                if not test:
                    return head
            result = ListNode(0, head)
            curr = result
            curr_end = result.next
            for _ in range(k - 1):
                tmp1 = curr.next     # tmp1 = 2 in [(2, 1), (3), 4]
                tmp2 = curr_end.next # tmp2 = 3 in [(2, 1), (3), 4]
                curr_end.next = curr_end.next.next
                curr.next = tmp2
                tmp2.next = tmp1
            return result.next

        result = ListNode(0)
        curr = result
        while True:
            curr.next = reverseK(head, k)
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return result.next
            head = head.next

# IDEA:
# first, need to look for a way to reverse a k-group of lists.
# consider when k = 4:
    # [(1), (2), 3, 4] -> [(2, 1), (3), 4] -> [(3, 2, 1), (4)] -> [4, 3, 2, 1]