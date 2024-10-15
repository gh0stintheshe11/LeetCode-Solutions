class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        from collections import Counter
        from math import comb
        
        MOD = 10**9 + 7
        freq = Counter(s)
        max_freq = max(freq.values())
        
        total = 0
        
        # Calculate number of good subsequences of each possible k
        for k in range(1, max_freq + 1):
            prod = 1
            for ch in freq:
                if freq[ch] >= k:
                    prod = (prod * (comb(freq[ch], k) + 1)) % MOD
            total = (total + prod - 1) % MOD
        
        return total