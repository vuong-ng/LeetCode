class Solution:
    def climbStairs(self, n: int) -> int:
        #redo 1
        memo = {}
        
        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = dp(i+1) + dp(i+2)
            return memo[i]
        return dp(0)



















        # res = 0
        # steps = collections.defaultdict()
        # def dfs(s):
        #     if s == n:
        #         return 1
        #     if s > n:
        #         return 0
        #     if s in steps: #already called the function
        #         return steps[s]
            
        #     steps[s] = dfs(s+1) + dfs(s+2)
        #     return steps[s]
        
        # return dfs(0)

        steps = {}
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in steps:
                return steps[i]
            steps[i] = dfs(i+1) + dfs(i+2)
            return steps[i]
        return dfs(0)

            

        