class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #REDO 1:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r,c,indx):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != word[indx] or (r,c) in visit:
                return False
            elif board[r][c] == word[indx]:
                visit.add((r,c))
                if indx == len(word)-1:
                    return True
                res= dfs(r+1,c,indx+1) or dfs(r-1,c,indx+1) or dfs(r, c+1,indx+1) or dfs(r,c-1,indx+1)
                visit.remove((r,c))
                return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0): return True
        return False










    # 1st time:
        # ROWS, COLS = len(board), len(board[0])
        # def backtrack(r, c, i):
        #     if i == len(word):
        #         return True
        #     if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r,c) in path:
        #         return False
            
        #     path.append((r,c))
        #     res = backtrack(r+1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r-1, c, i+1) or backtrack(r, c-1, i+1)
        #     path.remove((r,c))
        #     return res
        
        # for r in range(ROWS):
        #     for c in range (COLS):
        #         if backtrack(r,c,0): return True
        # return False

        
            

        
        