# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create two pointers the "heads"
        # compare the two values, choose the lower one, pop it and add to a new list
        # go until both pointers are null
        merged = ListNode()
        mergedHead = merged

        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged.next = ListNode(list2.val)
                list2 = list2.next
            merged = merged.next
        if list1:
            merged.next = list1;
        else:
            merged.next = list2
        return mergedHead.next