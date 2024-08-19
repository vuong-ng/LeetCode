class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0 , len(nums)-1
        index = collections.defaultdict()
        for i, v in enumerate(nums):
            index[v] = i
        for i,n in enumerate(nums):
            compl = target - n
            if compl in index and index[compl] != i:
                return [i, index[compl]]

        

        