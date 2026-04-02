# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # intuition here is that every node must fall within the restrictions given to it by its
        # parents. This means that we want to update its restrictions every time we go down a level
        # Since we have to track all of the ancestors to each node, we want to use a recursive DFS solution
        # In our recursive call, we need to update its boundaries as the left child's upper bound is node.val
        # and its right child's lower bound is node.val
        # so will go through a DFS solution updating the correct boundaries as we go (as each level
        # has boundaries that build from its parents) and then return False if the boundaries are ever 
        # not fulfilled
        def valid(root, leftBound, rightBound) -> bool:
            if not root:
                return True
            # if not valid, then return false
            if root.val <= leftBound or root.val >= rightBound:
                return False
            # if it is valid, return the validity of its children
            return valid(root.left, leftBound, root.val) and valid(root.right, root.val, rightBound)
        return valid(root, float("-inf"), float("inf"))