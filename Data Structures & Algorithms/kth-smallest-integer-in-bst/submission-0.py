# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if you use DF in order search, you need to return the kth element that you check
        # maybe just have a loop, and a counter for how many you pop from the stack, then when that counter
        # 
        # we can actually just traverse through the array normally using DFS, and then inOrder, add each
        # value to an array, which then will store the k value once we reach it
        popped = 0
        stack = []
        curr = root
        
        while curr or stack:
            # for this method, we want to go as far left as possible, adding each of the parents to 
            # the stack. Then, after reaching the most left, pop from the stack to "process" that value
            # then after that, go into the right tree
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            popped += 1
            if popped == k:
                return curr.val
            curr = curr.right