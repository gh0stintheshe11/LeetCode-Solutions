from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos = nums.index(k)
        
        # Transform nums into the new array with 1 for numbers greater than k, -1 for less, and 0 for k itself.
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        
        result = 0
        for i in range(n):
            if nums[i] > k:
                prefix_sum += 1
            elif nums[i] < k:
                prefix_sum -= 1
            
            if i >= pos:
                result += prefix_count[prefix_sum] + prefix_count[prefix_sum - 1]
                
            if i < pos:
                prefix_count[prefix_sum] += 1
        
        return result