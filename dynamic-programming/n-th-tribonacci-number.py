class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def dp(i):
            if i < 0:
                return 0
            if i == 0:
                return 0
            if i < 3:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dp(i-3) + dp(i-2) + dp(i-1)
            return memo[i]
        return dp(n)
        