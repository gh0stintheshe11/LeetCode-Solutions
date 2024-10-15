from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        degree = max(count.values())
        min_length = float('inf')
        
        for num in count:
            if count[num] == degree:
                min_length = min(min_length, last[num] - first[num] + 1)
        
        return min_length