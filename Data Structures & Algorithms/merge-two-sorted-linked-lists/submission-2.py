# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # need a head node, and a node that i'm adding onto
        head = curr_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            
            curr_node = curr_node.next
        
        curr_node.next = list1 or list2
        return head.next
        
        # loop through both the lists until one of them is empty
        # for each val, add the lesser one to a new list

        # after the loop, append the non-empty list onto the new list