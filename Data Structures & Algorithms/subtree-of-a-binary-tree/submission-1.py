# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # recursively call this method until the node's val and subroot
        # equal in value, then call a helper function
        # the helper function performs depth first search to see if they are
        # the same

        if root is None:
            return False
        if subRoot is None:
            return True
        
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, root, subRoot) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)