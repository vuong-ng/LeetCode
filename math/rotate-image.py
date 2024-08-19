class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # group transfer
        n = len(matrix)
        for r in range(n//2 + n%2):
            for c in range(n//2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[n-1-c][r]
                matrix[n-1-c][r] = matrix[n-1-r][n-1-c]
                matrix[n-1-r][n-1-c] = matrix[c][n-1-r]  
                matrix[c][n-1-r] = tmp

        # import deepcopy
        # copy1 = matrix.copy()
        # copy = copy1.copy()
        # col = len(matrix)-1
        # for r in range(len(matrix)):
        #     # col = len(matrix)-1
        #     print(col)
        #     for c in range(len(matrix)):
        #         print(r,c, "then", c, col)
        #         # print("then")
        #         matrix[c][col] = copy[r][c]
            # col-=1
        
        