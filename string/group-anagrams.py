class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        res, hashmap = [], {}
        for w in strs:
            wS = "".join(sorted(w))
            if wS not in hashmap:
                hashmap[wS] = [w,]
            else:
                hashmap[wS].append(w)
        for j in hashmap:
            res.append(j)
        return res
        """
        #count as hashmap key
        res = defaultdict(list) #dont have to deal with when the there is no count in the res dict
        for s in strs:
            count = [0] * 26
            for c in s:
                count[(ord(c) - ord("a"))] +=1
            if tuple(count) not in res:
                res[tuple(count)] = [s,]
            else:
                res[tuple(count)].append(s)
             #res[tuple(count)].append(s) #  a list can't be a dictionary key => convert to tuple
        return res.values()
        




