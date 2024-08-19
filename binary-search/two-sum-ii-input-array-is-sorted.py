class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[r] + numbers[l] == target:
                return [l+1,r+1]
            elif numbers[r] +numbers[l] < target:
                l+=1
            else:
                r-=1 
        return []























        # l,r = 0, len(numbers)-1
        # while l < r:
        #     if numbers[l] + numbers[r] == target:
        #         return [l+1, r+1]
        #     elif numbers[l] + numbers[r] < target:
        #         l+=1
        #     else:
        #         r-=1
        





















        # # i, j = 0, len(numbers)-1
        # # while i < j:
        # #     if numbers[i] + numbers[j] > target:
        # #         j -= 1
        # #     elif numbers[i] + numbers[j] < target:
        # #         i += 1
        # #     elif numbers[i] + numbers[j] == target:
        # #         break
        # # return [i+1,j+1]
        