from typing import List

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Primes less than 30
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        # Create a dictionary for prime factor masks
        def prime_mask(n):
            mask = 0
            for i, prime in enumerate(primes):
                if n % (prime * prime) == 0:
                    return -1
                elif n % prime == 0:
                    mask |= (1 << i)
            return mask
        
        prime_masks = [prime_mask(n) for n in range(31)]
        
        # DP array
        dp = [0] * (1 << len(primes))
        dp[0] = 1  # the empty subset is always valid
        
        # Fill the DP array
        for num in nums:
            num_mask = prime_masks[num]
            if num_mask == -1:
                continue
            
            # Iterate backwards to not use the same number twice in calculation
            for mask in range((1 << len(primes)) - 1, -1, -1):
                if (mask & num_mask) == 0:
                    dp[mask | num_mask] = (dp[mask | num_mask] + dp[mask]) % MOD
        
        # Exclude the empty subset
        result = (sum(dp) - 1) % MOD
        return result