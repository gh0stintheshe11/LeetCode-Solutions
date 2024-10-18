class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] + ([-float('inf')] * k)
        max_strength = -float('inf')

        for i in range(1,n+1):
            temp_dp = [0] + ([-float('inf')] * k)
            for j in range(1, min(k,i)+1): # Can have at most k subarrays or i if i < k 
                sign = 1 if j & 1 else -1 

                v1 = dp[j]   + sign * (k-j+1) * nums[i-1]
                v2 = dp[j-1] + sign * (k-j+1) * nums[i-1]

                temp_dp[j] = max(v1,v2)

            dp = temp_dp
            max_strength = max(max_strength, dp[-1]) # Take max across all dp[-1] for max strength
        
        return max_strength