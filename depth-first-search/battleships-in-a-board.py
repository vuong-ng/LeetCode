class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited=set()
        count=0
        def dfs(row, col):
            if row >= (len(board)) or row < 0 or col >= (len(board[0])) or col < 0 or board[row][col] != "X" or (row, col) in visited:
                return 
            visited.add((row, col))
            dfs(row+1, col)
            dfs(row-1,col)
            dfs(row, col+1)  
            dfs(row, col-1)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) not in visited and board[r][c]=="X":
                    dfs(r,c)
                    count+=1
        return count
        