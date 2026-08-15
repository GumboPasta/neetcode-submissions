# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy

        # split our linked lists in two
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # store start of second half and cut 1st half
        curr = slow.next
        prev = slow.next = None

        # reverse second list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # populate new linked list
        first = head
        second = prev
        
        while second:
            # store both next values
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # update pointers
            first = tmp1
            second = tmp2