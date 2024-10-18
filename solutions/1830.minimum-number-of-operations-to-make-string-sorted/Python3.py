class Solution:
    def makeStringSorted(self, s: str) -> int:
        freq = [0]*26
        for c in s: freq[ord(c) - 97] += 1
        
        MOD = 1_000_000_007
        fac = cache(lambda x: x*fac(x-1)%MOD if x else 1)
        ifac = cache(lambda x: pow(fac(x), MOD-2, MOD))
        
        ans, n = 0, len(s)
        for c in s: 
            val = ord(c) - 97
            mult = fac(n-1)
            for k in range(26): mult *= ifac(freq[k])
            for k in range(val): ans += freq[k] * mult
            n -= 1
            freq[val] -= 1
        return ans % MOD