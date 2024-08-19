class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # approach 1: one-pass 
        p0 = 0
        p2 = len(nums)-1
        curr = 0
        while curr <= p2:
            if nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            elif nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr +=1
            else: curr += 1        
        
        # approach 2: hash table
        # colors = collections.defaultdict(int)
        # for n in nums:
        #     colors[n] += 1
        # i = 0
        # while i < len(nums):
        #     if colors[0]:
        #         nums[i] = 0
        #         colors[0] -=1
        #     elif colors[1]:
        #         nums[i] = 1
        #         colors[1] -=1
        #     elif colors[2]:
        #         nums[i] = 2
        #         colors[2] -=1
        #     i+=1
                
            


        