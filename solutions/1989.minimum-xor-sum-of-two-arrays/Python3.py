class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        from functools import lru_cache
        n = len(nums1)
        
        @lru_cache(None)
        def dp(mask):
            i = bin(mask).count('1')
            if i == n:
                return 0
            min_xor = float('inf')
            for j in range(n):
                if not mask & (1 << j):
                    min_xor = min(min_xor, (nums1[i] ^ nums2[j]) + dp(mask | (1 << j)))
            return min_xor

        return dp(0)