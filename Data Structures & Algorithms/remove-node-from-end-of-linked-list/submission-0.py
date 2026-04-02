# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force would be to traverse through the entire array to get its length
        # then subtract n from that value, and traverse again to get the specific node, and remove it
        # O(2n)

        # could reverse it as well, then find the nth node, remove it, and then reverse it again

        # could also use two pointers, where the right is n places away from the left.
        # then just shift both of them in sync, until the right the end, and left is at the node
        # you want to remove. To do easier, we can have the left pointer be n+1 places away, such that
        # when right reaches the end, left.next needs to be replaced (no prev stored needed)
        # since we can't really do 2 things ahead, lets just a dummy node in the beginning, 
        # so that we can start it further away
        dummy = ListNode()
        dummy.next = head
        l, r = dummy, head
        for _ in range(n):
            r = r.next
        
        while r:
            r = r.next
            l = l.next
        
        # we have to remove l.next
        l.next = l.next.next
        return dummy.next
        
        
