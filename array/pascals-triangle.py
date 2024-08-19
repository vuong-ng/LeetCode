class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(numRows):
            temp = [0 for _ in range(row+1)]
            temp[0], temp[-1] = 1, 1

            for r in range(1, len(temp)-1):
                temp[r] = res[-1][r-1] + res[-1][r]
            res.append(temp)
        return res

        

        