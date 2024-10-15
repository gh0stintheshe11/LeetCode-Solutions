from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_count = defaultdict(int)
        pair_count = 0
        
        for num in nums:
            gcd1 = gcd(num, k)
            for gcd2 in gcd_count:
                if gcd1 * gcd2 % k == 0:
                    pair_count += gcd_count[gcd2]
            gcd_count[gcd1] += 1

        return pair_count