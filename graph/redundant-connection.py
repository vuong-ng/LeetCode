class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        size = [1] * (len(edges)+1)

        def find(n):
            # p = par[n]
            while n != par[n]:
                n = par[par[n]]
                # p = par[p]
                # n = par[par[n]]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            elif size[p1] > size[p2]:
                par[p2] = par[p1]
                size[p1] += size[p2]
            else:
                par[p1] = par[p2]
                size[p2] += size[p1]

            return True
        
        for u,v in edges:
            if find(u) == find(v):
                return [u,v]
            else: union(u,v)
            

        # visit = set()
        # red = []
        # graph = {i:[] for i in range(1,len(edges)+1,1)}
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)


        # def dfs(v):
        #     if v in visit:
        #         return
        #     visit.add(v)
        #     for u in graph[v]:
        #         if u in visit:
        #             red.append([v,u])  
        #         else: dfs(u)

        # if len(edges) > 0:
        #     dfs(1)
        # if red == []:
        #     return red
        # for e in range(len(edges)-1,-1,-1):
        #     if edges[e] in red:
        #         return edges[e]
        # # if red == []:
        # #     return red
        