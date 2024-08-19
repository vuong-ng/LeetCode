class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low+high)//2
            hours = 0
            for p in piles:
                h_per_pile = math.ceil(p/mid)
                #if h_per_pile > mid//p:
                #    h_per_pile = mid//p + 1
                hours += h_per_pile
            if hours <= h:
                high = mid - 1
                res = min(res, mid)
            else:
                low = mid + 1

        return res

                