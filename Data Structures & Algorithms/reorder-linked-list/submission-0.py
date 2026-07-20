class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Key Data Structure: Linked List (Fast and Slow Pointers)

        # Phase 1: find the middle of the list using fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next        # slow moves 1 step
            fast = fast.next.next   # fast moves 2 steps — when fast hits end, slow is at middle

        # Phase 2: reverse the second half of the list
        second = slow.next      # second half starts just after the middle
        prev = slow.next = None # cut the list in half (slow.next = None ends the first half)
        while second:
            tmp = second.next   # save next node before overwriting pointer
            second.next = prev  # reverse the pointer
            prev = second       # advance prev
            second = tmp        # advance second

        # Phase 3: merge the two halves by interleaving
        first, second = head, prev  # first = head of first half, second = head of reversed second half
        while second:               # second half is always shorter or equal, so drive loop with it
            tmp1, tmp2 = first.next, second.next  # save both next pointers before overwriting
            first.next = second     # insert second half node after first half node
            second.next = tmp1      # connect back to the rest of the first half
            first, second = tmp1, tmp2  # advance both pointers

        # Time Complexity: O(n) — three linear passes over the list
        # Space Complexity: O(1) — just pointers, no extra structures