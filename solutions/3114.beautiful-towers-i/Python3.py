from typing import List

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        max_sum = 0
        
        # Try each index as the peak of the mountain
        for i in range(n):
            total = heights[i]
            min_left = heights[i]
            min_right = heights[i]
            
            # Calculate non-decreasing up to peak i
            for j in range(i - 1, -1, -1):
                min_left = min(min_left, heights[j])
                total += min_left
                
            # Calculate non-increasing from peak i
            for j in range(i + 1, n):
                min_right = min(min_right, heights[j])
                total += min_right
                
            max_sum = max(max_sum, total)
        
        return max_sum