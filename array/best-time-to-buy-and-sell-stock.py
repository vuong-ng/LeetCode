class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        i,j = 0,0
        res = 0
        while j < len(prices):
            res = max(res, prices[j]-prices[i])
            if prices[j] < prices[i]:
                i=j
            j+=1
        return  res















        # redo 1
        res = 0
        if len(prices) <= 1:
            return 0
        i,j = 0,0
        while j < len(prices):
            if prices[i] > prices[j]:
                i+=1
            res = max(res, prices[j]-prices[i])
            j+=1











        res = 0
        i, j = 0, 0
        if len(prices) == 1:
            return 0
        while j < len(prices):
            res = max(res,prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
            j+=1
        return res 
            


















        #re-do 1
        b,s=0,0
        res = 0
        while s < len(prices):
            res = max(res, prices[s]-prices[b])
            if prices[s] < prices[b]:
                b = s
            s+=1
        return res

















        """
        min_price = float("inf")
        max_prof = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif prices[i] - min_price > max_prof:
                max_prof = prices[i] - min_price
        return max_prof
        """
        #sliding window technique
        # l, r = 0, 1
        # maxP = 0
        # while r < len(prices):
        #     if prices[r] < prices[l]:
        #         l = r
        #     elif maxP < prices[r] - prices[l]:
        #         maxP = prices[r] - prices[l]
        #     r+=1
        # return maxP
        
