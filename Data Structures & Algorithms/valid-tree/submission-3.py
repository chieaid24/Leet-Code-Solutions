class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree is only connected to a layer one above, and one below it,
        # no nodes allow skipping.
        # create some graph representation of the undir edges, maybe a hashap?
        # Starting from the node 0, for ease, we create a visited set of visited nodes
        # then we step through each of the children of 0. If any of the children are connected to 
        # a visited node (not including its direct parent) then we return False
        # So our DFS function can have currNode, parent, visited. returns a Bool
        # once it reaches all of the nodes w/o returning False, we know it must be valid.
        # Also, every node must be connected somehow for it to be True.f ie check if visited set at
        # the end's len = n.

        # Let's create an adjacency list to rep. our graph: HashMap(int: List(int))
        adjMap = defaultdict(list)
        for i, j in edges:
            adjMap[i].append(j)
            adjMap[j].append(i)
        
        # run our dfs starting at node 0.
        visit = set()
        def dfs(curr: int, parent: int) -> bool:
            visit.add(curr)
            for nei in adjMap[curr]:
                if nei == parent:
                    continue
                elif nei in visit:
                    return False
                else:
                    # call dfs again on this one
                    if dfs(nei, curr) == False:
                        return False
            return True

        # if this returns False, then I have to return false, else, then check for the length
        if not dfs(0, -1):
            return False
        return len(visit) == n

