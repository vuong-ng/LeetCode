class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp (i, sum_so_far):
            if i == len(nums) and sum_so_far == target:
                return 1
            if i > len(nums) - 1:
                return 0
            if (i, sum_so_far) in memo:
                print(i, '\t', sum_so_far)
                return memo[(i, sum_so_far)]
            # print(i, '\t',sum_so_far)
            memo[(i, sum_so_far)] = dp(i+1, sum_so_far - nums[i]) + dp(i+1, sum_so_far + nums[i])
            return memo[(i, sum_so_far)]
        return dp(0,0)

        