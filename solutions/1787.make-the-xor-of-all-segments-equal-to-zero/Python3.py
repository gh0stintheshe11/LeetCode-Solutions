from typing import List
from collections import Counter, defaultdict

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        max_val = 1 << 10  # nums[i] < 2^10
        dp = [float('inf')] * max_val
        dp[0] = 0
        
        for i in range(k):
            count = Counter()
            for j in range(i, len(nums), k):
                count[nums[j]] += 1
            
            total = sum(count.values())
            temp_dp = [min(dp)] * max_val
            
            for x in range(max_val):
                for num, cnt in count.items():
                    temp_dp[x] = min(temp_dp[x], dp[x ^ num] - cnt)
            
            dp = [x + total for x in temp_dp]
        
        return dp[0]