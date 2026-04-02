# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force -> add all nodes to a tuple, sort, then add to a new
        # linked list o(n) but lots of space

        # loop through list once, keep track of curr and prev, create a temp
        # that = to curr, then make curr.next = prev. Then prev = curr, 
        # prev = temp
        
        prev, curr = None, head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        