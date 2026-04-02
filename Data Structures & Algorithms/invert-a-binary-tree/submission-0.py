# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # at a high level: for each branch, swap node.left and node.right
        # cant we just do breadth first traversal, swapping each of them
        # can use a queue? 

        # recursion or iteration? 

        # create a queue
        Q = Queue()
        if root:
            Q.put(root)
        else:
            return root

        while not Q.empty():
            # check if it has children -> if so, swap them, and then add
            # them to the queue
            node = Q.get()
            if node.left or node.right:
                # swap the children
                temp = node.right
                node.right = node.left
                node.left = temp

                #add each of them to the Q
                if node.left:
                    Q.put(node.left)
                if node.right:
                    Q.put(node.right)
        return root

            


