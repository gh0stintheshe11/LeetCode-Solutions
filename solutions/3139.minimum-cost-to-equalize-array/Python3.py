import math
from typing import List

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10**9 + 7
        maxv = max(nums)
        d = [maxv - num for num in nums]
        if 2 * cost1 <= cost2:
            return (cost1 * sum(d)) % MOD
        n = len(nums)
        if n == 1:
            return (cost1 * sum(d)) % MOD
        if n == 2:
            return (cost2 * min(d) + cost1 * (max(d) - min(d))) % MOD
        maxd = max(d)
        r = sum(d) - maxd
        res = float('inf')
        if maxd <= r:
            res = (r + maxd) // 2 * cost2 + (r + maxd) % 2 * cost1
            maxd += 1
            r += n - 1
            res = min(res, (r + maxd) // 2 * cost2 + (r + maxd) % 2 * cost1)
            return res % MOD
        res = r * cost2 + (maxd - r) * cost1
        k = math.floor((maxd - r) / (n - 2))
        maxd += k
        r += (n - 1) * k
        res = min(res, r * cost2 + (maxd - r) * cost1)
        maxd += 1
        r += (n - 1)
        res = min(res, (r + maxd) // 2 * cost2 + (r + maxd) % 2 * cost1)
        maxd += 1
        r += n - 1
        res = min(res, (r + maxd) // 2 * cost2 + (r + maxd) % 2 * cost1)
        return res % MOD