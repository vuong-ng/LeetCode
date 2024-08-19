class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        # p1 points at s
        # p2 points at t
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i+=1
                j+=1
            else:
                i +=1
            # if p1 == len(s):
            #     return True
        return j == len(s)