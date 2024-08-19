class Solution:
    def rob(self, nums: List[int]) -> int:
        # redo 2
        ## bottom-up
        memo = [0] * (len(nums) + 1)

        memo[len(nums)] = 0
        memo[len(nums)-1] = nums[-1]
        for n in range(len(nums)-2, -1, -1):
            memo[n] = max(nums[n]+memo[n+2], memo[n+1])
        return memo[0]

        


        #redo 1
        ## top-down
        # memo = {}
        # def dp(i):
        #     if i > len(nums) - 1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(nums[i] + dp(i+2), dp(i+1))
        #     return memo[i]
        # return dp(0)
        ## top-down
        # memo = {}
        # def dfs(i):
        #     if i > len(nums)-1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(nums[i]+dfs(i+2), dfs(i+1))
        #     return memo[i]
        # if len(nums) < 2:
        #     return max(nums)
        # # return max(dfs(0), dfs(1))
        # return (dfs(0))
        