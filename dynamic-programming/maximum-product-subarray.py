class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        min_so_far = nums[0]
        max_so_far = nums[0]
        res = max_so_far
        for i in range(1, len(nums)):
            temp_max = max(nums[i], nums[i] * min_so_far, nums[i] * max_so_far)
            min_so_far = min(nums[i], nums[i] * min_so_far, nums[i] * max_so_far)
            max_so_far = temp_max
            res = max(res, max_so_far)
        return res
        
            
        