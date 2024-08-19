class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        substr = set()
        res = 0
        if len(s) == 0:
            return 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            res = max(res, len(substr))
        return res

















        #brute force
        """
        start = 0
        end = 0
        res = 0
        for i in range(len(s)):
            c = set()
            res = max(res, 1)
            for j in range(i,len(s)):
                if s[j] not in c:
                    c.add(s[j])
                else:
                    break
                res = max(res, j-i+1)
        return res
        """
        # sliding window O(n)
        start = 0
        charSet = set()
        res = 0
        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start+=1
            charSet.add(s[end])
            res = max(res, end - start + 1)
        return res
                
        
                