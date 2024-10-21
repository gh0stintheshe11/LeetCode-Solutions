from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        distinct_averages = set()
        n = len(nums)
        for i in range(n // 2):
            avg = (nums[i] + nums[n - 1 - i]) / 2
            distinct_averages.add(avg)
        return len(distinct_averages)