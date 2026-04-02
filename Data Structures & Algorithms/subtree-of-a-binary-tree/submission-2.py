# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # larger function loops through the root, calling a separate function to check if each node in main tree
        # is equal to the passed subtree

        # base case with root
        if not subRoot:
            return True
        if not root:
            return False
        
        # recursive call to other function
        if self.isSametree(root, subRoot):
            return True
        # check again going down the root
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recursive testing if root and subRoot are equal trees, using DFS

        # base case
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        
        return self.isSametree(root.right, subRoot.right) and self.isSametree(root.left, subRoot.left)

