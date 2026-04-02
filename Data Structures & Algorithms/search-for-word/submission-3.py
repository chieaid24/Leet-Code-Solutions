class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # brute force it by DFS through every letter on the board
        # in the dfs, we need to track the current cell, and also the index i that we are looking
        # for in the word
        # also track the current path that we've taken to continue on that
        # we need a set to track the tuple of cells that are in our current
        currPath = set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            # base case if we found the word
            if i == len(word):
                return True
            # base case if we went out of bounds, or incorrect letter in general
            if (r < 0 or 
                c < 0 or
                r >= ROWS or
                c >= COLS or
                board[r][c] != word[i] or
                (r, c) in currPath):
                return False
            # we know it is a valid letter
            currPath.add( (r, c) )
            # search all of the neighbors
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i+ 1) or dfs(r, c + 1, i+ 1) or dfs(r, c - 1, i+ 1)
            # if it is false then we can just clean up the path by removing this now
            currPath.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False