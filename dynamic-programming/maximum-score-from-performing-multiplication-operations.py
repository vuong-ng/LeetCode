class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = {}
        def dp(i,j):
            if j > len(multipliers)-1:
                return 0
            if i > len(nums)-1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = max(multipliers[j] * nums[i] + dp(i+1,j+1), multipliers[j] * nums[len(nums)-1-j+i] + dp(i,j+1))
            return memo[(i,j)]
        return dp(0,0)


















        # memo = {}
        # n = len(nums)
        # def dp(i, left):
        #     if i > len(multipliers) - 1:
        #         return 0
        #     if left > len(nums) - 1:
        #         return 0
            
        #     if (i,left) in memo: 
        #         return memo[(i,left)]
        #     memo[(i,left)] = max(multipliers[i]*nums[left] + dp(i+1, left+1), multipliers[i]*nums[n-1-(i-left)] + dp(i+1, left))
        #     return memo[(i,left)]
        # return dp(0,0)
        