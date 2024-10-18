from typing import List

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        initial_sum = sum(nums1)
        
        combined = sorted([(nums2[i], nums1[i]) for i in range(n)])
        nums2_sorted, nums1_sorted = zip(*combined)
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + nums1_sorted[i - 1] + nums2_sorted[i - 1] * j)
        
        for t in range(n + 1):
            if initial_sum + sum(nums2_sorted) * t - dp[t] <= x:
                return t
                
        return -1