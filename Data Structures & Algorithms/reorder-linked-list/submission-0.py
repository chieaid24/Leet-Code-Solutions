# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # brute force: loop through it to find the last value, remove it and add it to the 
        # res linked list. For every node I add to the res list, pop from original. 
        # O(n^2) since we visit every node, and for the end nodes, we must traverse the entire 
        # array -> basically be like if index is odd, pop from front. If index is even, pop from back.

        # better:we want somehow to have the end half of our array reversed, ie pointing backwards now
        # This is so then we can traverse with two pointers, and add from the front, then add
        # from the back and so on.
        # To do this, we would need to split the list into halves (first and second half)
        # We can actually do this using a fast and slow pointer, such that when the fast pointer gets
        # to the end, we know that the slow pointer will be pointing at the boundary at the half
        # way mark.

        # first we have to find the middle to partition the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow.next is our boundary (should be broken)

        # now, let's reverse the second part of the list
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head
        # now, lets start building our response with our first, and now second list
        while first and second:
            # add first, then add second
            firstTemp = first.next
            first.next = second
            first = firstTemp

            secondTemp = second.next
            second.next = first
            second = secondTemp
            


