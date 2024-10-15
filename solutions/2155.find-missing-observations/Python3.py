from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        totalRolls = n + m
        total_sum = mean * totalRolls
        observed_sum = sum(rolls)
        missing_sum = total_sum - observed_sum
        
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        result = [missing_sum // n] * n
        remaining = missing_sum % n

        for i in range(remaining):
            result[i] += 1

        return result