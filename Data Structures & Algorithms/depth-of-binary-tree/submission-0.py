# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recursiveDepth(node) -> int:
            # check if it has child nodes
            if not node:
                return 0
            return 1 + max(recursiveDepth(node.left), recursiveDepth(node.right))
        # create a recurive function, such that every call to the depth
        # it adds one to a count
        # 
        # as it calls the child nodes, does the max depth between the two nodes
        return recursiveDepth(root)

        