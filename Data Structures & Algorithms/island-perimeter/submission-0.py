class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Traverse through each grid using DFS, add all of the perimeters of its surrounding
        # tiles. For every boundary that you find (goes into the ocean) return 1 as your perimeter
        # Make sure to have a set of tuples of visited tiles
        visited = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            # if this is in ocean tile (out of bounds or =0), then return 1, since it is a boundary
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            elif (r, c) in visited:
                return 0
            # else this is a land tile, so mark it as visited
            visited.add((r, c))
            # now recursive step go to all 4 directions from the cell, and add all their perimeters
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        # we have to find the first land mass, and then call dfs from that
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
