class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {(len(s),0):True}
        def dp(i, left):
            if i >= len(s) or left < 0:
                return left==0
            if (i,left) in memo:
                return memo[(i,left)]
            if s[i] == "(":
                memo[(i,left)] = dp(i+1, left+1)
            elif s[i] == ")":
                memo[(i,left)] = dp(i+1, left-1)
            else:
                memo[(i,left)] = dp(i+1, left+1) or dp(i+1, left-1) or dp(i+1, left)
            return memo[(i,left)]
        return dp(0,0)

            

        