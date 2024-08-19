class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):  #change the position of each number in the nums list
            n = nums.pop(0)  # keep the number that is popped
            permutations = self.permute(nums) # returns a list of lists of permutation of the remaining numbers
            for j in permutations:
                j.append(n)
            res.extend(permutations)
            nums.append(n)
        return res

        # res = []
        # if len(nums) == 1:
        #     return [nums.copy()]
        # for i in range(len(nums)):
        #     n = nums.pop(0)
        #     permutations = self.permute(nums)
        #     for p in permutations:
        #         p.append(n)
        #     res.extend(permutations)
        #     nums.append(n)
        # return res

