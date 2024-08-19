class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        outdegree = [0]*(n+1)
        indegree = [0]*(n+1)
        for a,b in trust:
            outdegree[a] = outdegree[a] + 1
            indegree[b] = indegree[b] + 1
        for i in range(1,n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i
        return -1


        # visited = [False] * n
        # res = -1
        # graph = collections.defaultdict(list)


        # def dfs(cur,des):
        #     if cur == des:
        #         return True
        #     elif not visited[cur-1]:
        #         visited[cur-1] = True
        #         for v in graph[cur-1]:
        #             if dfs(v, des):
        #                 return True
        #     return False
        
        # if len(trust) == 0:
        #     if n == 1:
        #         return 1
        #     else:
        #         return -1
        # for i in range(1,n+1):
        #     if i != trust[0][1]:
        #         graph[i] = []
        # for a,b in trust:
        #     graph[a].append(b)
        # for n in graph:
        #     if trust[0][1] not in graph[n]:
        #         return res

        # for i in range(1,len(trust)):
        #     if dfs(trust[0][1], trust[i][0]): #if the judge trust anybody, there is no judge
        #         break
        #     elif i == len(trust)-1:
        #         res = trust[0][1]
        # return res
