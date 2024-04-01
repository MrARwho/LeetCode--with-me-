class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len(matrix)*len(matrix[0])-1
        
        while (end>= start):
            mid = (start + end) // 2
            mid_value = matrix[mid // len(matrix[0])][mid % len(matrix[0])]

            if mid_value == target:
                return True
            elif mid_value < target:
                start = mid + 1
            else:
                end = mid - 1        
        return False
    
