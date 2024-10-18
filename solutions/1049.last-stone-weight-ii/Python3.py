from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_weight = sum(stones)
        target = total_weight // 2
        
        dp = [0] * (target + 1)
        
        for stone in stones:
            for weight in range(target, stone - 1, -1):
                dp[weight] = max(dp[weight], dp[weight - stone] + stone)
                
        return total_weight - 2 * dp[target]