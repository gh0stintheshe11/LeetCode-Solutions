from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        max_val = 100
        n = len(nums)
        
        # Prepare prefix sums for each value from 1 to 100
        prefix_counts = [[0] * (max_val + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for v in range(1, max_val + 1):
                prefix_counts[i + 1][v] = prefix_counts[i][v]
            
            prefix_counts[i + 1][nums[i]] += 1
        
        # Answering each query
        result = []
        
        for li, ri in queries:
            prev = -1
            min_diff = float('inf')
            
            # Checking differences between present numbers in range
            for v in range(1, max_val + 1):
                count_in_range = prefix_counts[ri + 1][v] - prefix_counts[li][v]
                
                if count_in_range > 0:
                    if prev != -1:
                        min_diff = min(min_diff, v - prev)
                    prev = v
            
            if min_diff == float('inf'):
                result.append(-1)
            else:
                result.append(min_diff)
        
        return result