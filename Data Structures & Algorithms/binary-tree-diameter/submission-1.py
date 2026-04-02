# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # this is just the height of the left subtree + height of the right subtree
        # maximum throughout the entire tree
        # maybe: breadth first search, and for each node, depth first search to find the 
        # max height of the left and right subtrees, find the max in the breadth first search (for every node)
        # I would do breadth first search (Q) and then helper recursive function to get
        # the height of each tree O(N^2)

        # lets have a member function called self.res that we can update as we do DFS through
        # the tree, getting the max diameter (leftHeight + rightHeight) at each node it goes through
        # Now we can do DFS through the entire thing, and then just return the member function which
        # can be updated at any point through our recursive stack
        self.maxDiam = 0
        # returns the height of the node
        def dfs(curr: Optional[TreeNode]) -> int:
            # base case
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            # update maxDiam
            self.maxDiam = max(self.maxDiam, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.maxDiam