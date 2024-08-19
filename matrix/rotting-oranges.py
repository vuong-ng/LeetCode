class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = []
        adjs=[(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        fresh_remain=fresh
        t = 0
        # visited=set()
        while q and fresh:
            t+=1
            for i in range(len(q)):
                row,col = q.pop(0)
                for dr, dc in adjs:
                    if dr+row in range(len(grid)) and dc+col in range(len(grid[0])) and grid[dr+row][dc+col] == 1:
                        grid[dr+row][dc+col]=2
                        fresh-=1
                        q.append((dr+row, dc+col))
        return t if fresh == 0 else -1













        q = []
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        t = 0
        while q and fresh:
            t += 1
            for i in range(len(q)):
                row, col = q.pop(0)
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    if dr+row in range(len(grid)) and dc+col in range(len(grid[0])) and grid[dr+row][dc+col] == 1:
                        fresh -= 1
                        grid[dr+row][dc+col] = 2
                        q.append((dr+row,dc+col))
        if fresh == 0:
            return t
        return -1




        

















        t = 0
        fresh = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2: 
                    q.append((i,j))
    
        while q and fresh:
            t+=1
            for r in range(len(q)):
                row, col = q.popleft()
                # visit.add((row,col))
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr, dc in directions:
                    if dr+row in range(len(grid)) and dc+col in range(len(grid[0])) and grid[dr+row][dc+col] == 1:
                        fresh -= 1
                        # t+=1
                        q.append((row+dr, col+dc))
                        grid[row+dr][col+dc] = 2
        if fresh == 0:
            return t
        return -1




















        # fresh = 0
        # q = deque()
        # rows, cols = len(grid), len(grid[0])
        # time = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2:
        #             q.append((r,c))
        # directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # while q and fresh:
        #     for i in range(len(q)):
        #         r, c = q.popleft()

        #         #traverse to all adjacent oranges
        #         for dr, dc in directions:
        #             if r+dr== rows or c+dc == cols or r+dr < 0 or c+dc < 0 or grid[r+dr][c+dc] != 1:
        #                 continue
        #             grid[r+dr][c+dc] = 2
        #             fresh -= 1
        #             q.append((r+dr, c+dc))
        #     time += 1
        # if fresh == 0: 
        #     return time
        # return -1