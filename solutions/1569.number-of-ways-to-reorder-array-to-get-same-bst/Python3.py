from math import comb
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        @lru_cache(None)
        def count_ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            left_ways = count_ways(tuple(left))
            right_ways = count_ways(tuple(right))
            
            total_ways = comb(len(left) + len(right), len(left))
            return (total_ways * left_ways % MOD * right_ways % MOD) % MOD
        
        return (count_ways(tuple(nums)) - 1) % MOD