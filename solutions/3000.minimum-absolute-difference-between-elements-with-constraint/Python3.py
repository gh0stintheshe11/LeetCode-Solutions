from sortedcontainers import SortedList
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sorted_list = SortedList()
        min_diff = float('inf')
        
        for j in range(n):
            if j >= x:
                sorted_list.add(nums[j - x])
            
            if sorted_list:
                pos = sorted_list.bisect_left(nums[j])
                
                if pos < len(sorted_list):
                    min_diff = min(min_diff, abs(sorted_list[pos] - nums[j]))
                
                if pos > 0:
                    min_diff = min(min_diff, abs(sorted_list[pos - 1] - nums[j]))
        
        return min_diff