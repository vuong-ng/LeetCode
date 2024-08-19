class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_num = max(nums)
        nums.sort()
        memo = {}
        def dp(n):
            if n > max_num:
                return 0
            # if n not in counter:
            #     return 0
            if n in memo:
                return memo[n]
            memo[n] = max(n*counter[n] + dp(n+2), dp(n+1))
            return memo[n]
        return dp(nums[0])
                
    
            
        