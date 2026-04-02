# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breadth first search, every iteration loop, create a list and append that list to 
        # a larger list
        # need some sort of marker to say this is the end of a level

        # the way we can do this is check the length of the Q in the beginning, and then
        # pop that amount from the Q while still appending
        # will look like a for loop in a while loop
        # go until the Q is empty in the large loop
        if not root:
            return []
        
        Q = deque()
        Q.append(root)
        res = []
        while Q:
            count = len(Q)
            levelList = []
            for _ in range(count):
                node = Q.popleft()
                levelList.append(node.val)
                # append children to the Q
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            if levelList:
                res.append(levelList)
        return res

