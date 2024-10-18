from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def countMultiples(up_to: int) -> int:
            n = len(coins)
            total = 0
            for mask in range(1, 1 << n):
                bits = bin(mask).count('1')
                multiple = 1
                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                if bits % 2 == 1:
                    total += up_to // multiple
                else:
                    total -= up_to // multiple
            return total
        
        low, high = 1, min(coins) * k
        while low < high:
            mid = (low + high) // 2
            if countMultiples(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low