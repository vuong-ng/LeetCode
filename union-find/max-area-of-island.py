class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # redo 2:
        res= 0
        visited=set()
        adjs=[(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 1:
                    temp=1
                    visited.add((r,c))
                    q=[(r,c),]
                    while q:
                        row, col = q.pop(0)
                        for dr, dc in adjs:
                            if (dr+row) in range(len(grid)) and (dc+col) in range(len(grid[0])) and (dr+row, dc+col) not in visited and grid[dr+row][dc+col]==1:
                                temp+=1
                                visited.add((dr+row,dc+col))
                                q.append((dr+row,dc+col))
                    res = max(res,temp)
        return res










        # redo 1
        res = 0
        visit = set()
        # dfs:
        def dfs(r, c):
            if (r,c) in visit or r > len(grid)-1 or r < 0 or c > len(grid[0])-1 or c < 0 or grid[r][c] != 1:
                return 0
            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r,c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = dfs(r,c)
                if res < area:
                    res = area
        return res
        # bfs:
        visit = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = 0
                if grid[r][c] == 1 and (r,c) not in visit:
                    visit.add((r,c))
                    area += 1
                    q = [(r,c),]
                    directions = [[0,1], [1,0], [-1,0], [0,-1]]
                    while q:
                        row, col = q.pop(0)
                        for dr, dc in directions:
                            if dr+row in range(len(grid)) and dc+col in range(len(grid[0])) and grid[dr+row][dc+col] == 1 and (dr+row, dc+col) not in visit:
                                area+= 1
                                q.append((row+dr,col+dc))
                                visit.add((dr+row, dc+col))
                    if res < area: res = area
        return res
























        res = 0
        visit = set()
        area = 0

        # def bfs(r, c):
        #     stack = []
        #     stack.append((r, c))
        #     visit.add((r, c))
        #     directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #     area = 0
        #     while stack:
        #         r, c = stack.pop()
        #         area += 1
        #         # area = area + grid[r][c]
        #         for dr, dc in directions: #traverse all adjacent nodes
        #             r = dr+r
        #             c = dc+c
        #             if (r in range(len(grid)) and c in range(len(grid[0]))) and (r,c) not in visit and grid[r][c]:
        #                 stack.append((r,c))
        #                 visit.add((r,c))
        #                 # area += grid[i][j]
        #     return area

        def dfs(r, c):
            if (r not in range(len(grid))) or (c not in range(len(grid[0]))) or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r-1,c) + dfs(r, c+1)+ dfs(r,c-1)
            
            # directions = [[0,1], [0,-1], [1,0], [-1,0]]
            # area = grid[r][c]
            # visit.add((r, c))
            # for dr, dc in directions:
            #     r = dr + r
            #     c = dc+ c
            #     area += dfs(r,c)
            # return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = dfs(i,j)
                res = max(res, area)
        return res

    