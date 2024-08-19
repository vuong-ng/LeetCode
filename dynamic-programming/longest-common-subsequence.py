class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #redo 1
        memo = {}
        def dp(i,j):
            if i > len(text1) -1 or j > len(text2)-1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]: 
                memo[(i,j)] = 1 + dp(i+1, j+1)
            else:
                memo[(i,j)] = max(dp(i+1, j), dp(i,j+1))
            return memo[(i,j)]
        return dp(0,0)
            
















        # dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
        # # dp[len(text2)][len(text1)] = 0
        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1,-1,-1):
        #         if text1[i] == text2[j]:
        #             dp[j][i] = 1 + dp[j+1][i+1]
        #         else:
        #             dp[j][i] = max(dp[j+1][i], dp[j][i+1])
        # return dp[0][0]


        # memo = {}
        # def dp(i,j):
        #     if i > len(text1) - 1 or j > len(text2) - 1:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if text1[i] == text2[j]:
        #         memo[(i,j)] = max(1 + dp(i+1,j+1), dp(i+1, j+1))
        #     else:
        #         memo[(i,j)] = max(dp(i, j+1), dp(i+1,j))
        #     return memo[(i,j)]
        # return dp(0,0)