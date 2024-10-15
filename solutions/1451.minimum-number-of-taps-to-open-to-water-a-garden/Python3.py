from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create an array to store the maximum distance that can be watered
        max_ranges = [0] * (n + 1)
        
        # Transform the ranges into the maximum right endpoint they can reach
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_ranges[left] = max(max_ranges[left], right)
        
        taps = 0
        current_end = 0
        farthest_end = 0
        i = 0
        
        # Greedily find the minimal number of intervals to cover [0, n]
        while current_end < n:
            while i <= current_end:
                farthest_end = max(farthest_end, max_ranges[i])
                i += 1
            if farthest_end <= current_end:
                return -1
            current_end = farthest_end
            taps += 1
        
        return taps