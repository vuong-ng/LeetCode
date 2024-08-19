class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 1
        while curr < len(nums):
            if nums[prev] >= nums[curr]:
                curr += 1
            else:
                nums[curr], nums[prev+1] = nums[prev+1], nums[curr]
                prev +=1
        return prev+1