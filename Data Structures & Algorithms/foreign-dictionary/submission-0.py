class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # we want to create a graph that represents this problem
        # we use a graph to represent the "order" of letters, such that it is a directed graph
        # and must be acyclic, since a letter that comes before another will be pointing to the next letter
        # Let's do this by first looping through each pair of the words, and adding to our adjacency
        # list, creating our graph of c: set of characters that it directly comes before

        # now, we must loop through this graph, to see if it is valid or not
        # a valid graph will have no loops (since that would create a circular dependency)
        # additionally, if the graph is not fully connected, that is okay, as we want to call
        # the outer dfs function on each of the nodes to check for this (adding each to the res)
        # lastly, if there are dependencies such that A -> C and A -> B -> C, we obviosuly don't want
        # C to come before B, but this may naturally happen if we use preorder traversal, like usual DFS
        # therefore, we want to apply topological sort, by using POST order traversal, ie searching to the 
        # end of the children (to the leaf nodes), then backtracking our way up and adding to the list that way
        # by doing this, we only add the "closest" parent to each leaf node, if there are multiple directions to go,
        # since post order will start from the level that is closer to the leaf node.
        # since we CAN have duplicate edges, we can't just track a single Visited set, so we must 
        # have a different technique where we make a dict from (c: bool) such that we can change the bool
        # whether or not the node is currently in the path (if it is, and we see it again, we can return False)
        # else, then we just exit

        # first, let's create our adjacency list
        # create our default list, with all of the unique characters in the words
        adj = {c:set() for word in words for c in word}

        # loop throguh each pair of words, we need to compare the letters by letters and at the first 
        # differing letter, then we add it to our adj list
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # pattern where we only want to loop through the shorter string, to avoid index out of bounds erros
            minLen = min(len(w1), len(w2))
            # edge case such that w1 is longer than w2 AND they share the same prefix (invalid input)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # step through the words from the beginning, until their letters don't match
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # add it to our adj list
                    adj[w1[j]].add(w2[j])
                    break

        # now implement our DFS 
        res = []
        visit = {} # c:bool, where if True=node on current path, and False=node visited
        def dfs(c) -> bool: # returns whether or not it is an invalid graph (True=invalid) 
            # base case -> deal with it in the layer above
            if c in visit:
                return visit[c]
            visit[c] = True
            # since post order, we want to call this on ALL the children before adding it to our res list
            # also, we'll be adding things in a reversed order, so we have to reverse it at the end
            for nei in adj[c]:
                if dfs(nei):
                    return True
            # append it to our res
            res.append(c)
            visit[c] = False
        
        # now we want to call dfs on EVERY character node, since we have to 1) deal with unconnected nodes
        # (they can be added in any order), and we are ABLE to start in the middle, since we are creating
        # our res backwards, so it will always say the leaf nodes FIRST, which is all that matters
        for c in adj.keys():
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

            


