# QUESTION:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        result = ListNode()
        curr = result

        while heap:
            val, origin_list = heapq.heappop(heap)
            curr.next = lists[origin_list]
            curr = curr.next
            lists[origin_list] = lists[origin_list].next
            if lists[origin_list]:
                heapq.heappush(heap, (lists[origin_list].val, origin_list))

        curr.next = None
        return result.next

# IDEA:
# If we just track indices and compare every time, we would have O(nk) time.
# Using a heap we can achieve O(n log k)!
    # Recall that for min/max heaps, insertion and pop is O(log n) time where n is # elem in heap.
