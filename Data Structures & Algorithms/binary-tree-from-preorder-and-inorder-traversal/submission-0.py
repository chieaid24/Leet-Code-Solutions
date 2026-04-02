# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use recursion such that we always know the first element of preorder array is a root node
        # then, we can find that root node in the inorder array. The # of elements to the left of that 
        # node is the number of nodes in the left subtree, so we can partition the rest of the preorder
        # array accordingly. We can then call the function again assigning .left and .right correctly
        
        # base case
        if not preorder or not inorder:
            return None
        
        # create the root node
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root