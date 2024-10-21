from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_pair_sum = 0
        for i in range(n // 2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n - 1 - i])
        return max_pair_sum