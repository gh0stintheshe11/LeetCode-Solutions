from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        result = [0] * len(nums)
        
        for indices in index_map.values():
            k = len(indices)
            if k == 1:
                continue
            
            prefix_sum = [0] * k
            prefix_sum[0] = indices[0]
            for i in range(1, k):
                prefix_sum[i] = prefix_sum[i - 1] + indices[i]
            
            total_sum_right = prefix_sum[-1]
            total_sum_left = 0
            
            for i in range(k):
                left_count = i
                right_count = k - i - 1
                if left_count > 0:
                    total_sum_left += indices[i - 1]
                total_sum_right -= indices[i]
                
                result[indices[i]] = (indices[i] * left_count - total_sum_left) + (total_sum_right - indices[i] * right_count)
        
        return result