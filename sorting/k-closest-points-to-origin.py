
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for p in points:
            p = [(p[0]**2) + (p[1]**2), p[0],p[1]]
            distance.append(p)
        heapq.heapify(distance)
        res = []
        while k > 0:
            r = heapq.heappop(distance)
            res.append([r[1], r[2]]) 
            k-=1
        return res


        
            
        
        
        