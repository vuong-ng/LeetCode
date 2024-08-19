class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        sublist = []
        def dfs(i, total):
            # if i > len(candidates)-1:
            #     return 
            if total == target:
                res.append(sublist.copy())
                return 
            elif total > target or i > len(candidates) - 1:
                return
            sublist.append(candidates[i])
            total += candidates[i]
            dfs(i, total)

            total -= candidates[i]
            sublist.pop()
            dfs(i+1, total)
        
        dfs(0,0)
        return res
            

        # res = []
        # sublist = []
        # def dfs(i, total):
        #     if total == target:
        #         res.append(sublist.copy())
        #         return
        #     elif total > target or i >= len(candidates):
        #         return
            
        #     sublist.append(candidates[i])
        #     total += candidates[i]
        #     dfs(i, total)
        #     #dfs(i+1)

        #     sublist.pop()
        #     total -= candidates[i]
        #     dfs(i+1, total)

        # dfs(0, 0)
        # return res
            