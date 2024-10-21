from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        n = len(nums)
        count = 0
        freq = defaultdict(int)
        
        for i in range(n):
            for j in range(n):
                freq[nums[i] & nums[j]] += 1
        
        for k in range(n):
            for key, value in freq.items():
                if nums[k] & key == 0:
                    count += value
        
        return count