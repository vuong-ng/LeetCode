class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # redo 2
        res = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # s = []
        visited=set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] =="1" and (r,c) not in visited:
                    q = [(r,c),]
                    visited.add((r,c))
                    while q:
                        row, col = q.pop(0)
                        for dr, dc in directions:
                            if (row+dr) in range(len(grid)) and (dc+col) in range(len(grid[0])) and grid[row+dr][col+dc] == "1" and (row+dr, col+dc) not in visited:
                                visited.add((row+dr, col+dc))
                                q.append((row+dr, col+dc))
                    res+=1
        return res

















        # redo 1
        visit = set()
        n = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    visit.add((r,c))
                    q = [(r,c),]
                    adjs = [(0,1),(1,0),(0,-1),(-1,0)]
                    while q:
                        row,col = q.pop(0)
                        for i, j in adjs:
                            if row+i in range(len(grid)) and col+j in range(len(grid[0])) and (row+i,col+j) not in visit and grid[row+i][col+j] =="1":
                                q.append((row+i,col+j))
                                visit.add((row+i, col+j))
                    n += 1
        return n










        # re-do 2:
        res = 0
        visit = set()
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visit.add((i,j))
            while q:
                row, col = q.popleft()
                direction = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in direction:
                    if row+dr in range(len(grid)) and col+dc in range(len(grid[0])) and grid[dr+row][col+dc] == "1" and (row+dr, col+dc) not in visit:
                        q.append((row+dr, col+dc))
                        visit.add((row+dr, col+dc))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visit and grid[i][j] == "1":
                    bfs(i,j)
                    res += 1
        return res

        




        # re-do 1: 
        # visit = set()
        # res = 0
        # def dfs(row, col):
        #     if (col < 0 ) or (row < 0) or (row > len(grid) - 1) or (col > len(grid[0]) - 1) or grid[row][col] == "0":
        #         return             
        #     if (row, col) in visit:
        #         return
            
        #     visit.add((row,col))
        #     direction = [(0,1), (1,0), (0, -1), (-1,0)]
        #     for i, j in direction:
        #         dfs(row+i, col+j)
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1" and (i,j) not in visit:
        #             res += 1
        #             dfs(i,j)
        
        # # res = dfs(0,0)
        # return res
    

            










        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # res = 0

        # def bfs(row, col):
        #     q = deque()
        #     q.append((row,col))
        #     visit.add((row,col))
        #     while q:
        #         r, c = q.popleft()
        #         # visit.add((r,c))
        #         directions = [[0,-1],[0,1], [-1,0],[1,0]]
        #         for dr, dc in directions:
        #             if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == "1" and (r+dr, c+dc) not in visit:
        #                 visit.add((r+dr,c+dc))
        #                 q.append((r+dr, c+dc))


        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j]=="1" and (i,j) not in visit:
        #             bfs(i, j)
        #             res += 1
        # return res
        