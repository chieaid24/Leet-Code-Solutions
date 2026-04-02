# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force, loop through each value of list2, compare to list1
        # and insert when possible
        # O(n^2)

        # create a new list. loop through both at the same time (while with
        # node1 exists or node2 exists) compare the two nodes, add the smaller
        # one to the list, exit loop and increment
        # O(n+n) -> O(n)
        head = None
        curr_node = None
        next_node = None
        list1_ptr = list1
        list2_ptr = list2

        while list1_ptr is not None and list2_ptr is not None:
            
            # check if head and curr_node exist (special case)

            # compare values, add the smaller one etc
            if list1_ptr.val <= list2_ptr.val:
                next_node = list1_ptr
                list1_ptr = list1_ptr.next
            else:
                next_node = list2_ptr
                list2_ptr = list2_ptr.next
            
            #if the list is empty
            if not head and not curr_node:
                curr_node = next_node
                head = curr_node
            else:
                curr_node.next = next_node
                curr_node = curr_node.next
                curr_node.next = None
                print(curr_node.val)

        # this is when one of the two lists is now empty
        if not list1_ptr and list2_ptr:
            # if list1 is empty, append the entirity of list2 onto the head
            if not head:
                head = list2_ptr
            else:
                curr_node.next = list2_ptr
        elif not list2_ptr and list1_ptr:
            if not head:
                head = list1_ptr
            else:
                curr_node.next = list1_ptr
        return head

