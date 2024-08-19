class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # visiting = set()
        visited = set()
        graph = {i:[] for i in range(n)}
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for j in graph[node]:
                if j == prev:
                    continue
                elif not dfs(j, node):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n

        # def dfs(node):
        #     if node in visited:
        #         return False
        #     visiting.add(node)
        #     for v in graph[node]:
        #         if v not in visiting:
        #             # visiting.add(v)
        #             if not dfs(v):
        #                 return False
        #     # visiting.remove(node)
        #     visited.add(node)
        #     return True
        # # visiting.add(0)
        # if dfs(0) and len(visited) == n:
        #     return True
        # return False