class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        Method1: 1 variable
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] == val:
                nums.remove(nums[i])
        return len(nums)
        '''
        i=0
        for e in nums:
            if e != val:
                nums[i]=e
                i+=1
        return i