from typing import List
from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # Prime numbers <= 30
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        # Valid number mask for products of distinct primes (avoiding squares > 1)
        def get_prime_mask(x):
            mask = 0
            for i, prime in enumerate(primes):
                if x % prime == 0:
                    mask |= (1 << i)
            return mask
        
        # Prime factorization of numbers <= 30 without repeated primes
        mask_map = {
            2: 1, 3: 2, 5: 4, 6: 3, 7: 8, 10: 5, 11: 16, 13: 32, 14: 9, 
            15: 6, 17: 64, 19: 128, 21: 10, 22: 17, 23: 256, 26: 33, 
            29: 512, 30: 7
        }
        
        counts = Counter(nums)
        dp = [0] * (1 << len(primes))
        dp[0] = 1
        
        # Iterate each valid num in `mask_map` for dynamic programming
        for num in range(2, 31):
            if num not in mask_map:
                continue
            mask = mask_map[num]
            count = counts[num]
            for prev_mask in range((1 << len(primes)) - 1, -1, -1):
                if (prev_mask & mask) == 0:
                    dp[prev_mask | mask] = (dp[prev_mask | mask] + dp[prev_mask] * count) % MOD
        
        total_subsets = sum(dp[1:]) % MOD  # Sum of all non-empty valid subsets
        
        # Handling the number of 1's in the `nums`
        power_of_2 = pow(2, counts[1], MOD)
        result = (total_subsets * power_of_2) % MOD
        return result