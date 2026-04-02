# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #solve in similar way to the diameter problem, where we have a maxPath member variable
        # that we access in any recursive call if the path is ever greater
        # Equation for a path: maxPathLeft + node.val + maxPathRight. If a maxPath is ever negative,
        # just remove it from the calcalation, since it's useless
        # Go down using DFS in order search
        self.res = float("-inf")
        def dfs(curr) -> int:
            if not curr:
                return 0
            left = max(dfs(curr.left), 0)
            right = max(dfs(curr.right), 0)
            print(curr.val, left, right)

            # first, lets treat curr as a root node
            self.res = max(self.res, left + right + curr.val)
            # then, lets return the value treating this node as a subnode
            print(curr.val, "returning", (curr.val + max(left, right)))
            return curr.val + max(left, right)

        dfs(root)
        return self.res


