# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force, add all of the nodes values to a tuple, sort it,
        # then create a new LL that contains those values

        # real solution. create a while loop that if either of lists are not empty,
        # add the smaller value to a node.next, with anotehr pointer to the head node
        # (use a dummy node so you can add nodes and have it still return null if 
        # no values inserted) then do node = node.next to increment it to add onto
        # it for the next node. At the end, one of the lists are empty, so 
        # have node's next be list1 'or' list2 so only the valid one is added

        head = curr_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                # add list1's node to the curr_node
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        curr_node.next = list1 or list2
        
        return head.next
