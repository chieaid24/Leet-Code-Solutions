# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we know that the ancestor must be between the two values (or equal to either)

        # we could track the height in a dict where we do TreeNode: height, because there
        # can be multiple ancestors to both
        
        # We know if a node is an ancestor of the two nodes if its value is in the middle of the two
        
        # basically, we just need to do a DFS search that finds the node that lies between the two values
        # this will be the lowest ancestor

        # three choices at each level, 
        # 1) the root is in the middle of the two values (includes equal to) -> return that root
        # 2) the root is greater than both values -> move to the left (smaller part of the tree)
        # 3) the root is less than both values -> move to the right
        
        while root:
            if root.val > p.val and root.val > q.val:
                # move to the left
                root = root.left
            elif root.val < p.val and root.val < q.val:
                # move to the right
                root = root.right
            else:
                # lies in the middle or on one of the boundaries
                return root
        return None