class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #hashmap
        """
        freq= {} 
        count = [[] for i in range(len(nums)+1)] #index strats from 0
        for n in nums:                           #O(n)
            freq[n] = 1 + freq.get(n,0)
        for n, c in freq.items():                #O(n)
            count[c].append(n)
        res = []
        for i in range(len(count)-1,-1,-1):      #O(n)
            for j in count[i]:                   #O(kn)
                res.append(j)
                if len(res) == k:
                    return res
        """

        #max heap
        c = Counter(nums)
        c = sorted(c.items(), key=lambda kv: (kv[1], kv[0])) #sort according to values
        res = []
        for i in range(len(c)-1,-1,-1):
            res.append(c[i][0])
            if len(res) == k:
                return res


        
