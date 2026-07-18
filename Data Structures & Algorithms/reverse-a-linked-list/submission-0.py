class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Key Data Structure: Linked List (Iterative Approach)
        cur = head   # pointer to current node we're processing
        prev = None  # will become the new "next" for each node (starts as None = new tail)

        # While cur is a node and not none
        while cur:
            temp = cur.next  # save next node before we overwrite the pointer
            cur.next = prev  # reverse the pointer — point current node backwards
            prev = cur       # advance prev to current node
            cur = temp       # advance cur to the next node (saved above)

        return prev  # cur is None, prev is the new head (last node we processed)

        # Time Complexity: O(n) — visit every node once
        # Space Complexity: O(1) — just two pointers, no extra structures