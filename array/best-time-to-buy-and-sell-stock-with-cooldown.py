class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        memo = {}
        def dp (i, state):
            if i > len(prices) -1:
                return 0
            if (i, state) in memo:
                return memo[(i, state)]
            elif state == 0:
                # isSold = False
                memo[(i,state)] =  dp(i+1, 1)
            elif state == 1:
                memo[(i, state)] = max(dp(i+1, 1), dp(i+1, 2)- prices[i])
            elif state == 2:
                memo[(i, state)] = max(dp(i+1,3), dp(i+1,0)+prices[i])
            elif state == 3:
                memo[(i, state)] = max (dp(i+1,3), prices[i]+ dp(i+1,0))
            # else: 
            #     memo[(i, isSold)] = max(prices[i] + dp(i+1, True), dp(i+1, False))
            # print(memo[(i, isSold)])
            return memo[(i, state)]
        return dp(0,1)
                

        