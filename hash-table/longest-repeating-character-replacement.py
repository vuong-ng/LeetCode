class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #sliding window
        """
        count = {}
        res = 0
        start = 0
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)

            if (end-start+1) - max(count.values()) > k:  #length of window minus the most freq 
                                                            #character
                count[s[start]] -= 1
                start +=1
            res = max(res, end-start+1)
        return res
        """

        #optimized sliding window
        res = 0
        start = 0
        count = {}
        maxF = 0
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            maxF = max(maxF, max(count.values()))
            if (end-start+1) - maxF > k:
                count[s[start]] -=1
                start +=1
            res = max(res, end - start + 1)
        return res

            





            

