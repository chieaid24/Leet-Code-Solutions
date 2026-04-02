# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointers -> one slow pointer increments by 1, fast inc. by 2
        # if they ever equal each other, then loop exists
        # if fast reaches the end, loop DNE
        if head.next is None:
            return False
        slow = head
        fast = head.next

        while fast and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

