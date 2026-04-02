class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force is checking every row, every col, every square 
        # to check a square, we can create a dict ( (r,c):set()) where r,c is the big index, not small index
        # 
        # -> O(3*9^2) -> O(1)

        # calculate rows
        for row in board:
            seen = set()
            for cell in row:
                if cell in seen:
                    print("rows", cell, seen)
                    return False
                if cell != ".":
                    seen.add(cell)
        
        # calcaulte columns
        for i in range(9):
            seen = set()
            for row in board:
                if row[i] in seen:
                    print("cols")
                    return False
                if row[i] != ".":
                    seen.add(row[i])
        # calculate sub-boxes
        # one big dict such that it is (cellX, cellY):hashSet
        seen = defaultdict(set)
        for i in range(9):
            for j in range(9):
                indexI = i // 3
                indexJ = j // 3
                if board[i][j] in seen[(indexI, indexJ)]:
                    print("squares")
                    return False
                if board[i][j] != ".":
                    seen[(indexI, indexJ)].add(board[i][j])
        return True
        


