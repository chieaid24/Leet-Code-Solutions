# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # option 1 while loop continuing towards the end of the linkedlist
        # create a set that contains all of the nodes, if the node
        # is visited again, you know there is a loop and return true
        # if node.next = null, return false
        # time O(n), (create a set) Space O(n)

        # option 2 - with loops slow and fast pointer. slow pointer incremented
        # by 1, fast pointer incremented by 2, since both pointers will be
        # trapped in the loop if it exists, they will equal at a point -> return
        # true. if one of the pointers points to null, then return false
        # time O(n), space O(1)

        slow, fast = head, head;

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


