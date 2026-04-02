"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # the logic for cloning graphs with DFS is to have a oldToNew map, which maps from the oldNode -> newNode, so that we can 
        # check if we've already created a clone of said node in the original graph. If not, then just create a copy, and we want to 
        # run DFS on all of its neighbors to create clones of those too, and return the copy.
        oldToNew = {}

        def dfs(node):
            # if the node exists in our map, then we can return the "new" node since we already made a copy of it ("seen" base case)
            if node in oldToNew:
                return oldToNew[node]
            
            # now we know that it is a "new" node, so let's create a copy of it, and then return it
            copy = Node(node.val)
            # add it to our oldToNew
            oldToNew[node] = copy
            
            # now iterate through node's children and create copies of those too for our copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None