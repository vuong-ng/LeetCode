class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = []
        # start to search at these rooms[r][c] == 0:
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0: 
                    gates.append([r,c])
        # print(gates)
        for row,col in gates:
            q = [(row,col),]
            visit = set()
            while q:
                r, c = q.pop(0)
                visit.add((r,c))
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    if dr+r in range(len(rooms)) and (dc+c) in range(len(rooms[0])) and rooms[dr+r][dc+c] > 0 and (dr+r,dc+c) not in visit:
                        if rooms[dr+r][dc+c] > rooms[r][c] + 1:
                            rooms[dr+r][dc+c] = rooms[r][c] + 1
                        visit.add((dr+r,dc+c))
                        q.append([dr+r,dc+c])
























        
        # rows, cols = len(rooms), len(rooms[0])
        # # distance = collections.defaultdict()
        # visit = set()
        # q = deque()

        # for r in range(rows):
        #     for c in range(cols):
        #         if rooms[r][c] == 0:
        #             q.append((r,c))
        #             visit.add((r,c))
        
        # directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # level = 1

        # while q:
        #     for t in range(len(q)):
        #         i, j = q.popleft()
        #         for dr, dc in directions:
        #             if i+dr < 0 or j+dc < 0 or i+dr == rows or j+dc == cols or rooms[i+dr][j+dc] == -1 or (i+dr, j+dc) in visit:
        #                 continue
        #             rooms[i+dr][j+dc] = level
        #             q.append((i+dr, j+dc))
        #             visit.add((i+dr, j+dc))

        #     level +=1 

        