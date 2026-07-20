class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Key Data Structure: Linked List (Two Pointers)

        dummy = ListNode()  # dummy head so we never have to special-case removing the first node
        dummy.next = head
        behind = ahead = dummy  # both start at dummy

        # move ahead n+1 steps so the gap between behind and ahead is exactly n+1
        # this means when ahead hits None, behind is sitting right BEFORE the node to remove
        for _ in range(n + 1):
            ahead = ahead.next

        # slide both pointers together until ahead falls off the end
        while ahead:
            behind = behind.next
            ahead = ahead.next

        # behind is now just before the target node — skip over it
        behind.next = behind.next.next

        return dummy.next  # return real head (handles case where head itself was removed)

        # Time Complexity: O(n) — one pass through the list
        # Space Complexity: O(1) — just two pointers, no extra structures