class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}
        def dfs(i):
            if i == len(s): # in case of double digit
                return memo[i]

            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]

            res = dfs(i + 1) #single digit
            if i+2 <= len(s) and int(s[i: i+2]) <= 26:
                res += dfs(i+2) # double digit
            memo[i] = res
            return memo[i]
        return dfs(0)

            


        
