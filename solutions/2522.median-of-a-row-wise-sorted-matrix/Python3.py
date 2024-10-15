from typing import List

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        def count_less_equal(mid):
            count = 0
            for row in grid:
                left, right = 0, len(row)
                while left < right:
                    mid_idx = left + (right - left) // 2
                    if row[mid_idx] <= mid:
                        left = mid_idx + 1
                    else:
                        right = mid_idx
                count += left
            return count
        
        m, n = len(grid), len(grid[0])
        total_count = m * n
        half_count = total_count // 2
        
        low, high = min(row[0] for row in grid), max(row[-1] for row in grid)
        
        while low < high:
            mid = low + (high - low) // 2
            if count_less_equal(mid) <= half_count:
                low = mid + 1
            else:
                high = mid
        
        return low