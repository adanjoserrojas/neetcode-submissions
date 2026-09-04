class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                left = 0
                right = len(matrix[row]) - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
        