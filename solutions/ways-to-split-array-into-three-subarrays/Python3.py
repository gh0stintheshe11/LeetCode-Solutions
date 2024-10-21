from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Compute prefix sum
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        total_ways = 0
        
        # Iterate over all possible first split points
        for i in range(1, n - 1):
            left_sum = prefix_sum[i]
            
            # Find the first position j such that left_sum <= prefix_sum[j] - left_sum
            j = bisect_left(prefix_sum, 2 * left_sum, i + 1, n)
            
            # Find the first position k such that prefix_sum[k] - left_sum > total_sum - prefix_sum[k]
            k = bisect_right(prefix_sum, (prefix_sum[n] + left_sum) // 2, i + 1, n)
            
            # Add the number of valid split points for current i
            total_ways = (total_ways + max(0, k - j)) % MOD
        
        return total_ways