from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            max_distance = max(max_distance, abs(current_max - min_val), abs(max_val - current_min))
            
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
            
        return max_distance