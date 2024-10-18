class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 1
        
        MOD = 10**9 + 7
        max_operations = n - k + 1
        
        return pow(2, max_operations, MOD)