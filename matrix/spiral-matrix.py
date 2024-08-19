class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited=set()
        res=[]
        def dfs(row,col,goingUp):
            if row < 0  or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or (row,col) in visited:
                return
            res.append(matrix[row][col])
            visited.add((row,col))
            if goingUp:
                dfs(row-1,col,True)
                dfs(row,col+1,False)
                dfs(row+1,col,False)
                dfs(row,col-1,False)
            else:
                dfs(row,col+1,False)
                dfs(row+1,col,False)
                dfs(row,col-1,False)
                dfs(row-1,col, True)
        dfs(0,0,False)
        return res
