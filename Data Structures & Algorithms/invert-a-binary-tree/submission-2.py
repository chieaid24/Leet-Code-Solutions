# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # breadth first pre-order search, breadth first -> use a queue
        # deque + append() and popleft()
        Q = deque()
        Q.append(root)
        if not root or (root.left is None and root.right is None):
            return root
        
        # loop through Q until empty
        while Q:
            # get next Q node, swap the children, add children to Q 
            node = Q.popleft()

            #swap children
            temp = node.right
            node.right = node.left
            node.left = temp

            if node.right:
                Q.append(node.right)
            if node.left:
                Q.append(node.left)
        return root
