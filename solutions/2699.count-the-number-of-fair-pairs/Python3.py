from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            l = bisect_left(nums, lower - nums[i], i + 1, n)
            u = bisect_right(nums, upper - nums[i], i + 1, n)
            count += u - l
        
        return count