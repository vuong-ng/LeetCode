class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        preMap = {i:[] for i in range(numCourses)}
        order =[]

        #create map
        for c, p in prerequisites:
            preMap[c].append(p)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                if crs not in order:
                    order.append(crs)       
                return True
            visit.add(crs)
            for c in preMap[crs]:
                if not dfs(c): return False
            preMap[crs] = []
            visit.remove(crs)
            order.append(crs)
            return True
        
        for i in range(numCourses):
            dfs(i)
        if len(order) != numCourses:
            return[]
        return order            
        