class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        q = []
        visit = set()
        res = 0
        for u,v,w in times:
            edges[u].append([v, w])
        q = [(0,k)]
        heapq.heapify(q)
        cost=0
        while q:
            t, v = heapq.heappop(q)
            if v in visit:
                continue
            cost = max(cost, t)
            visit.add(v)
            for node, time in edges[v]:
                if node not in visit:
                    heapq.heappush(q, [time+cost, node])
                    # visit.add(node)
        return cost if len(visit) == n else -1




        
        

















        edges = collections.defaultdict(list)
        q = [(0,k)]
        cost = 0
        visit = set()

        for s,t,w in times:
            edges[s].append((w,t))

        while q:
            w,u = heapq.heappop(q) # pop min
            if u in visit:
                continue
            cost = max(cost, w)

            visit.add(u)
            if u in edges:
                for w2,n2 in edges[u]:
                    if n2 not in visit:
                        heapq.heappush(q, (w2 + w, n2))
        
        return cost if len(visit) == n else -1


        

        