# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first pass: use two pointers, one at the start of each list, add the two values at the pointers
        # and create a node is the res list that reflects this
        # if there is ever a overflow (> 9) store this in a global variable to use in the next iteration, and subtract 10 from the total
        # Loop until both lists are empty and also overflow is empty 
        # O(n + m) time O(1) extra space not including the response space

        dummyHead = ListNode()
        curr = dummyHead

        carry = 0

        while l1 or l2 or carry:
            # init the values at each index
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # add them and create a new node with that value
            sum = val1 + val2 + carry
            # can't be below 10
            carry = sum // 10
            curr.next = ListNode(sum % 10)

            # increment all pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummyHead.next