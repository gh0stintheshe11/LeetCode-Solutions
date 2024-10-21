class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def solve(idx, m1, m2):
            if idx == -1: return 0

            a, b = nums1[idx], nums2[idx]
            if m1 < min(a, b) or m2 < min(a, b): return float('inf')
        
            s1, s2 = float('inf'), float('inf')
            if a <= m1 and b <= m2: s1 = solve(idx - 1, m1, m2)
            if b <= m1 and a <= m2: s2 = 1 + solve(idx - 1, m1, m2)

            return min(s1, s2)
        
        n = len(nums1)
        if n == 1: return 0

        sol = min(solve(n - 2, nums1[-1], nums2[-1]), 1 + solve(n - 2, nums2[-1], nums1[-1]))
        return -1 if sol == float('inf') else sol