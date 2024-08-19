class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_rows = set()
        for r in range(len(matrix)):
            min_temp = matrix[r][0]
            for c in range(len(matrix[0])):
                min_temp = min(min_temp, matrix[r][c])
            min_rows.add(min_temp)
        max_temp = 0
        for c in range(len(matrix[0])):
            max_temp = matrix[0][c]
            for r in range(len(matrix)):
                max_temp = max(matrix[r][c], max_temp)
            if max_temp in min_rows:
                return [max_temp]