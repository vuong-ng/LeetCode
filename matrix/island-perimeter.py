class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # perimeter at each cell on the island: 4 - number of neighbor cells
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    directions = [(0,1),(1,0),(0,-1),(-1,0)]
                    temp = 4
                    for dr, dc in directions:
                        if (i+dr) in range(len(grid)) and (j+dc) in range(len(grid[0])) and grid[i+dr][j+dc] == 1:
                            temp-=1
                            # visited.add((i+dr,j+dc))
                    res+=temp
        return res
        