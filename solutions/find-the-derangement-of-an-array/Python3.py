class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        derangements = [0] * (n + 1)
        derangements[1] = 0
        derangements[2] = 1
        
        for i in range(3, n + 1):
            derangements[i] = (i - 1) * (derangements[i - 1] + derangements[i - 2]) % MOD
        
        return derangements[n]