# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # brute force -> loop through both trees with depth/breadth first search
        # create an array with each of those values, traverse through the array
        # to find better
        # O(n) time, O(n) space (very inefficient)
        #
        # second attempt
        # traverse through the root tree until finds a node with value == subroot
        # follow the 'same tree' bfs with 2 queues to check for equality. if at any point
        # returns false, exit out of this loop and continue traversing through root
        # once it gets to the end return false
        
        def equalTree(node, subRoot) -> bool:
            nodeQ = deque([node])
            subRootQ = deque([subRoot])

            while nodeQ and subRootQ:
                # maintain that you're checking both trees' corresponding
                # layer at a time
                for _ in range(len(nodeQ)):
                    node_node = nodeQ.popleft()
                    subRoot_node = subRootQ.popleft()

                    if node_node is None and subRoot_node is None:
                        continue
                    if node_node is None or subRoot_node is None or node_node.val != subRoot_node.val:
                        return False
                    
                    # append all
                    nodeQ.append(node_node.right)
                    nodeQ.append(node_node.left)
                    subRootQ.append(subRoot_node.right)
                    subRootQ.append(subRoot_node.left)
            return True


        # traverse through root tree checking values
        rootQ = deque([root])

        while rootQ:
            node = rootQ.popleft()
            if node is None:
                continue
            
            if node.val == subRoot.val:
                # function that searches through each
                equal = equalTree(node, subRoot)
                if equal:
                    return True
            rootQ.append(node.left)
            rootQ.append(node.right)
        return False