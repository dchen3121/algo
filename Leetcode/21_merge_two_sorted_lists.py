# QUESTION:
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        result = ListNode(0, l1)
        curr = result

        while curr.next and l2:
            if curr.next.val < l2.val:
                curr = curr.next
            else:
                tmp = l2
                l2 = l2.next
                tmp.next = curr.next
                curr.next = tmp
                curr = curr.next
        if l2:
            curr.next = l2
        return result.next

# soln = Solution()
# print(soln.mergeTwoLists([1], [2]))
# print(soln.mergeTwoLists([1, 2, 4], [1, 3, 4]))
