from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix_sum = 0
        index_map = {}
        max_length = 0
        
        for i in range(len(hours)):
            if hours[i] > 8:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            if prefix_sum > 0:
                max_length = i + 1
            else:
                if prefix_sum - 1 in index_map:
                    max_length = max(max_length, i - index_map[prefix_sum - 1])
                if prefix_sum not in index_map:
                    index_map[prefix_sum] = i
        
        return max_length