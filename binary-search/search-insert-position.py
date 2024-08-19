class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        last = len(nums)-1
        first = 0
        while last >= first:
            mid = (last+first)//2
            if target > nums[mid]:
                first = mid + 1
            elif target < nums[mid]:
                last = mid - 1
            else:
                return mid
        return first