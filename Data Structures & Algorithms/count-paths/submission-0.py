class Solution:

    def inBounds(self, i, j, rows, cols) -> bool:
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False
        return True

    def uniquePaths(self, m: int, n: int) -> int:
        # Brute force:
        # create a m x n grid called dp. Then we dfs starting from 0,0 and search right and down 
        # one tile. For every tile that we hit, we incremenet its dp entry by 1 (no visited set)
        # return the entry in the last cell of dp
        # time ? space O(n * m) (some repeated work)

        # optimizations? 
        # start from the end
        # we are doing BFS, probably iteratively starting from the last cell, and going left and up
        # for each cell that we evaluate, we set its value to its right cell + its bottom cell, as
        # this builds the # of paths to get to the end, starting from the current cell (ie, # of paths
        # if it goes right + # of paths if it goes left)
        # We probably just use a Q for BFS, such that we make sure that the grid is as up to date as possible
        # when calculating "deeper" paths.
        # we need to keep a "visited" set as well, as we should only visit each cell once
        
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        visited = set() # set of tuples (int, int)
        Q = deque([(m - 1, n - 1)]) # list of tuples (int, int)
        while Q:
            # calculate its value
            i, j = Q.popleft()
            if not self.inBounds(i, j, m, n) or (i, j) in visited:
                continue
            visited.add((i, j))
            
            dp[i][j] += dp[i + 1][j] if self.inBounds(i + 1, j, m, n) else 0
            dp[i][j] += dp[i][j + 1] if self.inBounds(i, j + 1, m, n) else 0

            # add its left and top neighbors to the Q
            Q.append((i - 1, j))
            Q.append((i, j - 1))
        return dp[0][0]

