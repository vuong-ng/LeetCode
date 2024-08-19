class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo= [1] * len(nums)

        # for i in range(len(nums)-1, -1,-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             memo[i] = max(memo[i], 1+ memo[j])
        # return max(memo)

        # build a subsequence
        sub = [nums[0],]
        for i in range(1,len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                for j in range(len(sub)):
                    if sub[j] >= nums[i]:
                        sub[j] = nums[i]
                        break
        return len(sub)


                        
        