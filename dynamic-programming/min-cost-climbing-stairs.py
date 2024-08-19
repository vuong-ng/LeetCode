class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def climb(i):
            if i > len(cost)-1:
                return 0
            if i == len(cost)-1:
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i] + climb(i+1), cost[i] + climb(i+2))
            return memo[i]
        return min(climb(0), climb(1))


















        # memo = {}
        # def dfs(i):
        #     if i < 0:
        #         memo[i] = min(dfs(i+1), dfs(i+2))
        #     if i > len(cost)-1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = min(cost[i] + dfs(i+1), cost[i] + dfs(i+2))
        #     return memo[i]
        # return dfs(-1)
        