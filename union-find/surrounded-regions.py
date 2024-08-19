class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # visit = set()
        kept = set()
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            if board[i][cols-1] == "O":
                kept.add((i,cols-1))
            if board[i][0] == "O":
                kept.add((i,0))
        
        for j in range(cols):
            if board[0][j] == "O":
                kept.add((0,j))
            if board[rows-1][j] == "O":
                kept.add((rows-1,j))

        #change all O that is not flipped to T
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O": 
                return

            board[r][c] = "T"
            # kept.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i, j in kept:
            dfs(i, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

                
        