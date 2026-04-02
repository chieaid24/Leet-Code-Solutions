# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # we can easily encode it by using , to separate our values, and N as a null value
    # encode with pre order traversal and make sure to include both nulls as characters so we know 
    # when to move to the next node when decoding

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        # do dfs through the tree, and add each node to the res, using pre-order traversal adding to our string
        def dfs(curr):
            if not curr:
                res.append("N")
                return
            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return ",".join(res)
    # 1,2,N,N,3,4,N,N,5,N,N
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.index = 0
        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(vals[self.index])
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        res = dfs()
        return res
