class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False

        # def backtrack(i, sum1, sum2):
        #     if i > len(nums) - 1:
        #         if sum1 == sum2:
        #             return True
        #         return False
        #     return backtrack(i+1, sum1+nums[i], sum2) or backtrack(i+1, sum1, sum2+nums[i])
        # return backtrack(0, 0,0)

        