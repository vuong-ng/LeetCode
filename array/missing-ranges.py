class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return [[lower, upper]]
    
        res = []
        i = 0
        if nums[0] > lower:
            res.append([lower, nums[0]-1])
        while i < len(nums) - 1:
            if (nums[i+1] - nums[i]) > 1:
                res.append([nums[i]+1, nums[i+1]-1])
            i+=1
        if nums[-1] < upper:
            res.append([nums[-1]+1, upper])
        return res
        

