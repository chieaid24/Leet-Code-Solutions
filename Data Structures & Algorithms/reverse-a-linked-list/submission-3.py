# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # have a curr, temp, prev pointers 
        # while curr has next, point curr to prev while keeping curr.next in temp
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        head.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        