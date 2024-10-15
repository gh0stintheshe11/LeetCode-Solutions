from typing import List
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = defaultdict(list)
        
        for num in nums:
            remainder = num % k
            groups[remainder].append(num)
        
        def count_k_free_subsets(arr: List[int]) -> int:
            n = len(arr)
            if n == 0:
                return 1
            if n == 1:
                return 2
            
            dp = [0] * (n + 1)
            dp[0] = 1
            dp[1] = 2
            
            for i in range(2, n + 1):
                if arr[i-1] - arr[i-2] == k:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1] * 2
            
            return dp[n]
        
        result = 1
        for group in groups.values():
            result *= count_k_free_subsets(group)
        
        return result