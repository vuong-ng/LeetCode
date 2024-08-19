class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(total, i, subset):
            if total == target :
                res.append(subset.copy())
                return 
            if total > target or i > len(candidates)-1 :
                # subset = []
                return
            total += candidates[i] 
            subset.append(candidates[i])
            dfs(total, i+1, subset)

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]: 
                # to skip duplicates in the list
                i+=1
            total -= candidates[i]
            subset.pop()
            dfs(total, i+1, subset)
        dfs(0,0,subset)
        return res



        # res = []
        # subset = []
        # candidates.sort()
        # def dfs(i, total, subset):
        #     if total == target:
        #         res.append(subset.copy())
        #         return
        #     if i >= len(candidates) or total > target:
        #         return
        #     subset.append(candidates[i])
        #     total += candidates[i]
        #     dfs(i+1, total, subset)

        #     while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
        #         i+=1

        #     subset.pop()
        #     total -= candidates[i]
        #     dfs(i+1, total, subset)

        # dfs(0, 0,[])
        # return res
        