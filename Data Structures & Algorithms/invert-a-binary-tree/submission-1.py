# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # breadth first search with a queue
        Q = deque()

        # loop until the Q is empty
        # pop the node from the queue, switch the two children, then add
        # the children back into the Q if they exist
        Q.append(root)
        
        while Q:
            # pop the value from the Q
            curr_node = Q.popleft()
            if not curr_node:
                return root
            # swap the two children
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            
            # now add each of the children to the Q if they exist
            if curr_node.left:
                Q.append(curr_node.left)
            if curr_node.right:
                Q.append(curr_node.right)
        return root
            


