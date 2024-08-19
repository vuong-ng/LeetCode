class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n+1)]
        # roots = []
        size = [1]*(n+1)
        
        def find(n):
            while n != par[n]:
                n = par[par[n]]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]
            return 1
        # n nodes but only n- # of nodes that got connected rrepresent the number of connected components
        res = n
        for u,v in edges:
            res -= union(u,v)
        return res
            
        