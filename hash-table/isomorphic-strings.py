class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #hash map
        """
        s_t = {}
        t_s = {}
        for i in range(len(s)):
            if (s[i] not in s_t) and (t[i] not in t_s):
                s_t[s[i]] = t[i]
                t_s[t[i]] =s[i]
            else:
                if (s_t.get(s[i]) != t[i]) or (t_s.get(t[i]) != s[i]): ##get check if the element in the map or doesnot match the letter
                    return False
        return True
        """
        #first occurance 
        def transform(s):
            m = {}
            res = []
            for i, c in enumerate(s):
                if c not in m:
                    m[c] = i
                res.append(str(m[c]))
            return " ".join(res)
        return transform(s) == transform(t) 
                
        
