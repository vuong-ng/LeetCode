class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if (len(s) != len(t)): return False
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] =1
        for j in range(len(t)):
            if t[j] in map and map[t[j]] > 0:
                map[t[j]] -=1
            else: return False
        return True
