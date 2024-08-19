class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        if len(nums) == 0:
            return res

        while i < len(nums):
            start = i
            while i < len(nums)-1 and nums[i] + 1== nums[i+1]:
                i+=1
 
            if nums[start]== nums[i]:
                s = str(nums[start])
            else:
                s = str(nums[start]) + "->" + str(nums[i])
            res.append(s)
            i+=1

        return res
        