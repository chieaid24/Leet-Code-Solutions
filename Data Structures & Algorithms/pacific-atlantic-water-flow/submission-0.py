class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # better solution: checking each cell is not ideal. Instead, lets start from the ocean
        # and get all the nodes that can access the ocean, for each ocean
        # then, let's compare these two sets and overlapping cells can reach both.
        NUM_ROWS, NUM_COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        # loop through all 4 directions, and since we will start at the edges through an outer loop
        # we can just return when it reaches the edge
        def dfs(i: int, j: int, visited: set[tuple[int, int]], prevHeight: int) -> None:
            # base cases
            if i < 0 or i >= NUM_ROWS or j < 0 or j >= NUM_COLS:
                return
            if (i,j) in visited:
                return
            if heights[i][j] < prevHeight:
                return
            # add this cell to visited
            visited.add((i, j))
            
            # loop through each direction
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        # let's do this by looping through all the cells on the top row after adding the correct
        # cells to our pacific visited hashmap:
        for j in range(NUM_COLS):
            dfs(0, j, pac, heights[0][j])
            dfs(NUM_ROWS - 1, j, atl, heights[NUM_ROWS - 1][j])
        
        # now loop through the left and right sides, adding them again to our P and A sets
        for i in range(NUM_ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, NUM_COLS - 1, atl, heights[i][NUM_COLS - 1])
        
        # now, both of our sets of all the cells that connect to either ocean is populated
        # so we can loop through all the cells in the grid, adding them to a res list
        res = []
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res

        


        # to make it simpler, our DFS function will only search up + down for each cell that is 
        # started from, since we will be looping through L + R in an outer loop