class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs:
        # explore from each cell
        # if the adjacent cell reached : add that cell into the result list. 
        # if there is a path from a cell to an ocean, all cells along that path can reach the ocean
        # redo 1
        pacifics= []
        atlantics = []
        for r in range(len(heights)):
            pacifics.append((r,0))
            atlantics.append((r,len(heights[0])-1 ))
        for c in range(len(heights[0])):
            pacifics.append((0, c))
            atlantics.append((len(heights)-1, c))
        
        res =[]
        def bfs(q):
            reachable = set()
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            while q:
                r,c = q.pop(0)
                reachable.add((r,c))
                for dr, dc in directions:
                    if dr+r in range(len(heights)) and dc+c in range(len(heights[0])) and (dr+r, dc+c) not in reachable and heights[dr+r][dc+c] >= heights[r][c]:
                        q.append((dr+r,dc+c))

            return reachable

        pacifics_reachable = bfs(atlantics)
        atlantics_reachable = bfs(pacifics)
        for e in pacifics_reachable:
            if e in atlantics_reachable:
                res.append(e)
        return res
















        if not heights:
            return []
        atlantic_q, pacific_q = [],[]
        for i in range(len(heights)):
            pacific_q.append((i,0))
            atlantic_q.append((i,len(heights[0])-1))
        for i in range(len(heights[0])):
            pacific_q.append((0,i))
            atlantic_q.append((len(heights)-1,i))
        result = []
        def bfs(q):
            reachable = set()
            while q:
                r,c = q.pop(0)
                reachable.add((r,c))
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in directions:
                    if dr+r in range(len(heights)) and dc+c in range(len(heights[0])) and (dr+r, dc+c) not in reachable:
                        if heights[dr+r][dc+c] >= heights[r][c]:
                            # reachable.add((dr+r,dc+c))
                            q.append((dr+r,dc+c))
            return reachable
        reachable_atlantics = bfs(atlantic_q)
        reachable_pacifics = bfs(pacific_q)
        for val in reachable_atlantics:
            if val in reachable_pacifics:
                result.append(val)
        return result







        # visit = set()
        res = []
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,prevHeight, visit):
            if r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeight or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1, c, heights[r][c], visit)
            dfs(r-1, c, heights[r][c], visit)
            dfs(r, c+1, heights[r][c], visit)
            dfs(r, c-1, heights[r][c], visit)
        
        #run dfs on top line and bottom line
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows-1, c, heights[rows-1][c], atl)
        
        #run the first column and the last column:
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols-1, heights[r][cols-1], atl)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res


        