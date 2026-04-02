# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # loop through the original list, for each value, the next one's .next
        # is the curr value, then when at last value, set that equal to head
        curr_node = head
        prev_node = None
        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node

        