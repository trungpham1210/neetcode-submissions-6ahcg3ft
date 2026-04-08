class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix) 
        col_len = len(matrix[0]) 

        low, high = 0, row_len*col_len - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // col_len][mid % col_len] == target:
                return True
            elif matrix[mid//col_len][mid % col_len] < target: 
                low = mid + 1
            else:
                high = mid - 1
        return False