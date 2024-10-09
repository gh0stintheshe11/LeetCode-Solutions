class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        max_val = (1 << p) - 1
        half_count = max_val // 2
        return (pow(max_val - 1, half_count, MOD) * max_val) % MOD