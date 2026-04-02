# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # first pass would be to just DFS or BFS through both, adding each to their respective arrays, then compare structures

        # I think you have to iterate through both of them
        # perform DFS

        stackP = [p]
        stackQ = [q]

        while stackP and stackQ:
            tempP = stackP.pop()
            tempQ = stackQ.pop()
            if not tempP and not tempQ:
                continue
            elif tempP and tempQ:
                if tempP.val != tempQ.val:
                    return False
                
                # append left and right
                stackP.append(tempP.right)
                stackP.append(tempP.left)

                stackQ.append(tempQ.right)
                stackQ.append(tempQ.left)
            else:
                return False


        if stackP or stackQ:
            return False
        return True

