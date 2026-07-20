class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Key Data Structure: Linked List (Fast and Slow Pointers)

        # Phase 1: find the middle using dummy node so slow stops at end of first half
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy  # both start at dummy, giving fast a head start

        while fast and fast.next:
            slow = slow.next        # slow moves 1 step
            fast = fast.next.next   # fast moves 2 steps

        # slow is now at the last node of the first half
        second = slow.next      # second half starts just after slow
        slow.next = None        # cut the list in half

        # Phase 2: reverse the second half
        prev = None
        while second:
            tmp = second.next   # save next before overwriting
            second.next = prev  # reverse the pointer
            prev = second       # advance prev
            second = tmp        # advance second

        # Phase 3: interleave first and reversed second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  # save both next pointers
            first.next = second     # insert second node after first node
            second.next = tmp1      # connect back to rest of first half
            first, second = tmp1, tmp2  # advance both pointers

        # Time Complexity: O(n) — three linear passes
        # Space Complexity: O(1) — just pointers, no extra structures