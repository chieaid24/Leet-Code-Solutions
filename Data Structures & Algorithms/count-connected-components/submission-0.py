class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # first pass: create adjacency list (int: list(int))
        # run dfs / bfs on it while tracking a visited set
        # same approach as # of islands, where everytime we call DFS, we increment our counter
        # time: o(n) where n is the number of edges space: o(n + m) where m in # of nodes
        # + o(n + m) for DFS through it, plus o(m) for the set. ie time: o(n + m) space, o(n + m)

        # second pass: run union find. Basically, we have a parent array par=[0 1 2 3 4]
        # and we have a rank array rank=[1 1 1 1 1]. Parent is the root parent of each node (specified by index)
        # and rank is the size of the "tree" that each node is the root of. This is to minimize the tree height
        # when connecting unions of different sizes (we want to add the smaller one to the larger one)

        # basically, we start with n nodes, and for every merge we do, we subtract 1 from the number of nodes
        # Loop through each edge, and find both nodes' parent. If they have the same root parent, then 
        # we can return early (since they are already connected). If they do not have the same root parent,
        # then we can connect them by setting the smaller rank node's parent as the larger rank node.  
        # additionally, when finding the parent node to a node, we want to collapse the tree as much as possible
        # (to speed up searches in the future) and we do this by if a node has a parent, then we set the parent
        # to be its grandparent -> flattens the tree by 1, since we know a grandkids' parent can be their grandparent.

        # create our arrays -> parent (tracks the parent of each node (index))
        parent = [i for i in range(n)]
        # rank -> the size of the tree that it is the root of
        rank = [1] * n
        
        # find parent function
        def findPar(n1) -> int:
            p1 = parent[n1]
            
            # go until the parent's parent = parent, ie we reached the top of the tree
            while p1 != parent[p1]:
                # flatten by 1 if we can
                parent[p1] = parent[parent[p1]]
                p1 = parent[p1]
            return p1
        
        # merge two numbers
        def union(n1, n2):
            p1, p2 = findPar(n1), findPar(n2)

            # if parents are the same, return 0 (no unions needed since they are already connected)
            if p1 == p2:
                return 0
            # now we merge, the smaller rank into the larger rank
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return 1
        
        # main loop
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
