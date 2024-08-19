class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        h = set(nums) # to avoid duplicates
        # for n in nums:
        #     h.add(n)
        res = 1
        for n in nums:
            l = 1
            if n-1 not in h: # n is in the middle of the seq
                # l+=1
                n+=1
                while n in h:
                    n+=1
                    l+=1
                if res < l:
                    res = l
        return res
            
            

        