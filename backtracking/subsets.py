class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        sublist = []
        def dfs(i):
            if i >= len(nums):
                res.append(sublist.copy())
                return
            sublist.append(nums[i])
            dfs(i+1)
            sublist.pop()
            dfs(i+1)
        dfs(0)
        return res 















        res = []
        sublist = []
        def dfs(i):
            if i > len(nums) - 1:
                res.append(sublist.copy())
                return 
            sublist.append(nums[i])
            dfs(i+1)
            sublist.pop() 
            dfs(i+1)
            
        dfs(0)
        return res




        # res = []
        # subset = []
        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy()) # append copy since subset constantly
        #                                   ## being modified => can change the 
        #                                   ### result that already appended
        #         return
            
        #     #include the element into the subset
        #     subset.append(nums[i])
        #     dfs(i+1)

        #     #not to include the element]
        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)
        # return res
        


