class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Key Data Structure: Fast and Slow Pointers
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy  # both start at dummy, fast moves 2x speed of slow

        while fast and fast.next:  # fast.next check prevents crash when fast is at last node
            fast = fast.next.next  # fast moves 2 steps
            slow = slow.next       # slow moves 1 step

            if slow is fast:  # if they meet, fast lapped slow — there's a cycle
                return True

        return False  # fast hit None — list has an end, no cycle

        # Time Complexity: O(n) — fast pointer reaches end or meets slow within n steps
        # Space Complexity: O(1) — just two pointers, no extra structures