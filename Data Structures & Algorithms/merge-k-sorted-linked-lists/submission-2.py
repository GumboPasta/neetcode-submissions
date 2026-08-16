import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        n = len(lists)

        # first the first nodes in each of the linked list
        for i, node in enumerate(lists):
            # if its a valid node
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # store new output
        D = ListNode()
        curr = D

        # populate new linked list
        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = node

            node = node.next

            if node:
                heapq.heappush(heap, (node.val, i, node))

        return D.next