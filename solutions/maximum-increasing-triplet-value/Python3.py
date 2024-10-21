from typing import List
import bisect

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[n-1] = nums[n-1]
        
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        
        seen = []
        max_value = float('-inf')
        
        for j in range(n):
            if right_max[j] > nums[j]:
                i = bisect.bisect_left(seen, nums[j])
                if i > 0:
                    max_value = max(max_value, seen[i-1] - nums[j] + right_max[j])
            bisect.insort(seen, nums[j])
        
        return max_value