# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        head = result

        carry = 0
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            carry = 0
            if curr_sum >= 10:
                curr_sum -= 10
                carry = 1
            head.next = ListNode(curr_sum)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr_sum = l1.val + carry
            carry = 0
            if curr_sum >= 10:
                curr_sum -= 10
                carry = 1
            head.next = ListNode(curr_sum)
            head = head.next
            l1 = l1.next
        while l2:
            curr_sum = l2.val + carry
            carry = 0
            if curr_sum >= 10:
                curr_sum -= 10
                carry = 1
            head.next = ListNode(curr_sum)
            head = head.next
            l2 = l2.next
        if carry:
            head.next = ListNode(1)

        return result.next
