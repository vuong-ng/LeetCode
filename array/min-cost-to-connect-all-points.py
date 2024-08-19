class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        # mst = []
        res = 0
        for i, p in enumerate(points):
            heap.append([float("inf"), p])
            # mst.append([float("inf"), p])
        heapq.heapify(heap)
        heap[0][0] = 0
        while heap:
            d, curr_point = heapq.heappop(heap)
            print(d)
            res += d
            for node in heap:
                if node[0] > abs(node[1][0] - curr_point[0]) + abs(node[1][1] - curr_point[1]):
                    node[0] = abs(node[1][0] - curr_point[0]) + abs(node[1][1] - curr_point[1])
                    heapq.heapify(heap)
        return res



















        q = []
        new_points = []
        for i in range(len(points)):
            new_points.append([float('inf'), points[i]])
            heapq.heappush(q, [float('inf'), points[i]])
        res = 0
        q[0][0] = 0
        while q:
            p = heapq.heappop(q)
            res += p[0]
            for node in q:
            
                if abs(p[1][0] - node[1][0]) + abs(p[1][1] - node[1][1]) < node[0]:
                    
                    node[0] = abs(p[1][0] - node[1][0]) + abs(p[1][1] - node[1][1])
                
                    heapq.heapify(q)
        return res



            
        