from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        
        for rod in rods:
            current_dp = dp.copy()
            for diff, height in current_dp.items():
                # Case 1: Add rod to the first support
                new_diff1 = diff + rod
                dp[new_diff1] = max(dp.get(new_diff1, 0), height)
                
                # Case 2: Add rod to the second support
                new_diff2 = abs(diff - rod)
                dp[new_diff2] = max(dp.get(new_diff2, 0), height + min(diff, rod))
        
        return dp[0]