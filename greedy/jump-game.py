class Solution:
    def canJump(self, nums: List[int]) -> bool:
        des = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= des:
                des = i
        if des == 0:
            return True
        return False
        ## Try DP next time (!)
        # def jump(i):
        #     if i >= len(nums) - 1:
        #         return True
        #     if i < len(nums) - 1 and nums[i] == 0:
        #         return False
        #     for j in range(nums[i]):
        #         if jump(i+j): 
        #             return True
        #         else:
        #             continue
        #     return False
        # return jump(0)
        # curT = 0
        # for i, n in enumerate(nums):
        #     if curT == 0 and i != len(nums) - 1 and n == 0:
        #         return False
        #     curT += n - 1
        # return True

        