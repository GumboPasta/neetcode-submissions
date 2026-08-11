# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        # Key Data Structure: Fast and Slow Pointers
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next: 
            # update our pointers
            slow = slow.next
            fast = fast.next.next

            # check if they ever collide
            if slow == fast:
                return True

        return False