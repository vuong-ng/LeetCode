class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1 
                        continue

                if nums[l] + nums[r] + nums[i] < 0:
                    l+=1
                else:
                    r-=1
        return res
                
            
        
        




        