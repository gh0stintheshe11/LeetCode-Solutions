from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        left, right = 0, n - 1
        
        while left <= right:
            mid_col = left + (right - left) // 2
            max_row = 0
            # Find the maximum element in the mid column
            for i in range(m):
                if mat[i][mid_col] > mat[max_row][mid_col]:
                    max_row = i

            # Check if it is a peak element
            left_is_smaller = mid_col == 0 or mat[max_row][mid_col] > mat[max_row][mid_col - 1]
            right_is_smaller = mid_col == n - 1 or mat[max_row][mid_col] > mat[max_row][mid_col + 1]
            
            if left_is_smaller and right_is_smaller:
                return [max_row, mid_col]
            elif not left_is_smaller:
                right = mid_col - 1
            else:
                left = mid_col + 1

        return [-1, -1]  # This line is just placeholder; the while loop should always return a valid peak