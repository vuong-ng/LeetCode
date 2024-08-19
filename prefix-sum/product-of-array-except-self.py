class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        next_1 = 1
        next_2 = 1
        from_end = []
        from_start = []
        j = len(nums)-1
        res = [0] * len(nums)
        for i in range(len(nums)):
            from_start.append(next_1)
            next_1 *= nums[i]
            from_end.append(next_2)
            next_2 *= nums[j]
            j-=1
        print(from_start)
        j = len(nums)-1
        for i in range(len(nums)):
            res[i] = from_end[j] * from_start[i]
            j-=1
        return res
