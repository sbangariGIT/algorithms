class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        row = 0
        n = len(matrix[0]) - 1
        while row < len(matrix):
            # check if in bounds
            if matrix[row][0] <= target and matrix[row][n] >= target:
                # its in this row
                l = 0
                r = n
                while l <= r:
                    mid = (l+r) // 2
                    if target == matrix[row][mid]:
                        return True
                    if target < matrix[row][mid]:
                        r = mid - 1
                    if target > matrix[row][mid]:
                        l = mid + 1
                return False
            else:
                row += 1
        return False