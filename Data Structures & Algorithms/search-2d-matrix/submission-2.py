class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix) - 1
        numCols = len(matrix[0]) - 1
        
        left, right = 0, numRows

        targetRow = -1

        while left <= right:
            middle = (right + left) // 2 # middle represents target
            if matrix[middle][0] <= target <= matrix[middle][numCols]:
                targetRow = middle
                break
            elif matrix[middle][0] < target:
                left = middle + 1
            elif target < matrix[middle][numCols]:
                right = middle - 1
        if targetRow == -1:
            return False
        
        left, right = 0, numCols
        while left <= right:
            middle = (right + left) // 2
            if matrix[targetRow][middle] == target:
                return True
            elif matrix[targetRow][middle] < target:
                left = middle + 1
            elif matrix[targetRow][middle] > target:
                right = middle - 1
            
        return False