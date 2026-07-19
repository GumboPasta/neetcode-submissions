class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        d = ListNode()  # dummy head node — gives cur a starting point so we never deal with an empty result list
        cur = d         # cur tracks the tail of the merged list, we append to it each step

        while list1 and list2:  # keep merging while both lists still have nodes
            if list1.val < list2.val:
                cur.next = list1   # attach the smaller node to the merged list
                cur = list1        # advance cur to the newly attached node
                list1 = list1.next # advance list1 past the node we just used
            else:
                cur.next = list2   # list2's node is smaller (or equal), attach it
                cur = list2        # advance cur to the newly attached node
                list2 = list2.next # advance list2 past the node we just used

        cur.next = list1 if list1 else list2  # one list is exhausted — attach the remainder of the other

        return d.next  # skip the dummy head, return the real merged list

        # Time Complexity: O(n + m) — visit every node in both lists once
        # Space Complexity: O(1) — just rearranging existing pointers, no new nodes