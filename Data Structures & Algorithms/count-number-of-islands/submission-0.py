class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs through it, once it exits, we know it is a single island
        # track all "seen" cells, and then loop through the entire
        # grid, calling DFS on each cell if == 1 and not in seen
        # then, after it exits the loop, increment the island counter
        seen = set()
        res = 0
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])

        def dfs(i, j):
            # base cases
            if i < 0 or i >= NUM_ROWS or j < 0 or j >= NUM_COLS:
                return
            if (i, j) in seen:
                return
            if grid[i][j] == "0":
                return
                
            seen.add((i, j))

            # recursive case
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    res += 1
        return res