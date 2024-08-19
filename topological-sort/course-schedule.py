class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i:[] for i in range(numCourses)}
        for k, val in prerequisites:
            map[k].append(val)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if map[crs] == []:
                return True
            visit.add(crs)
            for c in map[crs]:
                if not dfs(c): return False
            visit.remove(crs)
            map[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True


        # map = collections.defaultdict()
        # self.time = 0
        # complete = set()
        # visit = set()

        # def dfs(n):
        #     visit.add(n)
        #     if n in complete or map[n] == []:
        #         return

        #     if self.time >= numCourses:
        #         self.impos = True
        #         return
        #     if n not in map or map[n] == n or if map[n] in visit: # n doesnt have prerequisite
        #         # self.taken+=1
        #         visit.add(n)
        #     dfs(map[n])

        # for k, val in prerequisites:
        #     if k not in map:
        #         map[k] = [val,]
        #     else:
        #         map[k].append(val)
        # # visit.add(0)
        # for key in map: 
        #     if key not in complete:
        #         dfs(key)
        # if self.impos == True:
        #     return False
        # return True
        



        