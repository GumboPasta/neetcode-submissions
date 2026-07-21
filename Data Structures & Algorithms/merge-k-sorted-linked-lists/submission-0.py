import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Key Data Structure: Min Heap + Linked List
        heap = []

        # seed the heap with the first node from each list
        # store (value, list_index, node) — list_index breaks ties when values are equal
        # since ListNode objects aren't comparable with < 
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        D = ListNode()  # dummy head so we always have a node to append to
        cur = D         # cur tracks the tail of the merged result

        while heap:
            val, i, node = heapq.heappop(heap)  # pull the smallest node across all lists
            cur.next = node  # attach it to the merged list
            cur = node       # advance cur to the newly attached node

            node = node.next  # look at the next node in the same list
            if node:
                heapq.heappush(heap, (node.val, i, node))  # push it into the heap to compete next

        return D.next  # skip dummy head, return real merged list

        # Time Complexity: O(n log k) — n total nodes, each pushed/popped from a heap of size k
        # Space Complexity: O(k) — heap holds at most one node per list at any time