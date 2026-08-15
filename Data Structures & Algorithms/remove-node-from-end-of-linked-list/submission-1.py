# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy

        # iterate a pointer at n+1 positions -> gap between our ahead and behind 
        for _ in range(n+1):
            ahead = ahead.next

        # while ahead is not None
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        # behind is directly before the target value
        behind.next = behind.next.next

        return dummy.next
