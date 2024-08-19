class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom-up
        dp = [[0] * (n+1)  for _ in range(m+1)]
        # dp[m-1][n-1] = 1
        for i in range(m-1, -1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]



        # top-down
        # memo = {}
        # def dp(i,j):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     elif i > m-1 or j > n -1:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     memo[(i,j)] = dp(i+1,j) + dp(i,j+1)
        #     return memo[(i,j)]
        # return dp(0,0)
        