# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1st solution is to create a set (hashmap) of nodes
        # that have been visited. if any nodes' .next is in the hashmap
        # then return true
        # else if all the nodes are visited, return false
        # O(n)

        # set of nodes that have been visited
        visited = set()
        node = head
        while node.next is not None:
            visited.add(node)
            if node.next in visited:
                return True
            node = node.next
        return False


