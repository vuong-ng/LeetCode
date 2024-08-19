class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n_col=len(matrix[0])-1
        l,r = 0, len(matrix)-1
        while l<=r:
            m = int((r-l)//2+l)
            if target > matrix[m][n_col]:
                l=m+1
            elif target < matrix[m][0]:
                r=m-1
            elif target == matrix[m][n_col] or target == matrix[m][0]:
                return True
            elif target > matrix[m][0] and target < matrix[m][n_col]:
                break
        left=0
        right=n_col

        while left <= right:
            mid = int((right-left)//2 + left)
            if matrix[m][mid] > target:
                right=mid-1
            elif matrix[m][mid] < target:
                left=mid+1
            elif target == matrix[m][mid]:
                return True
        return False















        #redo 1
        # found = False
        # choose row 
        n_row = len(matrix)-1
        n_col = len(matrix[0])-1
        l, r = 0, n_row
        while l <= r:
            # print(l, r)
            m = int(((r-l)/2)+l)
            if target > matrix[m][n_col]:
                # print(matrix[m][n_col])
                l = m+1
            elif target < matrix[m][0]:
                # print(matrix[m][0])
                r = m-1
            elif target == matrix[m][0] or target == matrix[m][n_col]:
                return True
            elif target > matrix[m][0] or target < matrix[m][n_col]:
                # row = m
                break
        row = m
        print(row)
        # choose col
        l,r = 0, n_col
        while l <= r:
            m = int(((r-l)/2)+l)
            if target == matrix[row][m]:
                return True
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
        return False









        # for row in range(len(matrix)):
        #     for col in range(len(matrix[row])):
        #         left = 0
        #         right = len(matrix[row])-1
        #         if target > matrix[row][right]:
        #             break
        #         else:
        #             while left <= right:
        #                 mid = (left+right)//2
        #                 if target < matrix[row][mid]:
        #                     right = mid - 1
        #                 elif target > matrix[row][mid]:
        #                     left = mid + 1
        #                 elif target == matrix[row][mid]:
        #                     return True
        # return False