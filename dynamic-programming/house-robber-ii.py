class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i, end):
            if i > end:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i+2, end), dfs(i+1, end))
            return memo[i]
        if len(nums) <= 1:
            return nums[0]

        res1 = dfs(0, len(nums) - 2)
        memo = {}
        res2 = dfs(1, len(nums)-1)
        return max(res1, res2)
        # return res

        