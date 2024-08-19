class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for adj in graph[node]:
                if dfs(adj):
                    return True
        return dfs(source)




        # visited = [False] * n
        # graph = collections.defaultdict(list)

        # def dfs(cur):
        #     if cur == destination:
        #         return True
        #     elif not visited[cur]:
        #         visited[cur] = True
        #         for v in graph[cur]:
        #             if dfs(v):
        #                 return True
        #     return False

        # for a,b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)
        # return dfs(source)




        # if len(edges) == 0:
        #     return True
        # visited = [False for i in range(len(edges))]
        # def dfs(src, destination):
        #     for e in range(len(edges)):
        #         if src in edges[e] and not visited[e]: #first edge containing the source
        #             visited[e] = True
        #             if edges[e][0] == src:
        #                 non_scr = edges[e][1]
        #             else:
        #                 non_scr = edges[e][0]
        #             if non_src == destination:
        #                 return True
        #             else: 
        #                 return dfs(non_src, destination)
        #     return False
        
        # for i in range(len(edges)): #go through all adjacent edges of source
        #     if source in edges[i]:
        #         visited[i] == True
        #         if edges[i][0] == source:
        #             non_src = edges[i][1]
        #         else:
        #             non_src = edges[i][0]
        #         if dfs(non_src, destination):
        #             return True
        # return False

                