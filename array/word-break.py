class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]



        # def strCompare(substr):
        #     if len(substr) <= 0:
        #         return True
        #     for w in wordDict:
        #         i = substr.find(w)
        #         if i != -1:
        #             if i + len(w) - 1 == len(substr)-1:
        #                 substr = substr[:i]
        #             else: 
        #                 substr = substr[:i] + substr[i+len(w):]
        #             if strCompare(substr):
        #                 return True
        #             # return strCompare(substr)
        #             else:
        #                 continue
        #     return False
        # return strCompare(s)
    