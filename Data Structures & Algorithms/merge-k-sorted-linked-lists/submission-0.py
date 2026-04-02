# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # first pass would be merge the first two, then the next and next, etc
        # O(n * m) where n is the length of lists, since the first list will be gone over n times

        # a better way to do this (reduce the amount of merges that we need to do)
        # is at each step, merge each list with the list next to it 
        # this divides the amount of lists by 2
        # leading to a O(N * logM) solution
        # go until there is only 1 list in lists

        # base case
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            # our lists that we have created during this iteration (dividing it by 2)
            tempLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                tempLists.append(self.mergeLists(l1, l2))
            lists = tempLists
        return lists[0]

    def mergeLists(self, l1, l2) -> ListNode:
        # merge two lists (leetcode easy)
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                # append l1, and increment l1
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                # append l2, and increment l2
                head.next = l2
                head = head.next
                l2 = l2.next
        # after this, if either list still exists, then append the rest, then return
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
