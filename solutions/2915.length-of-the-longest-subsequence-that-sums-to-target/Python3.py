class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0  # Base case: sum is 0 with length 0
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]  # Not taking nums[i-1]
                if j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - nums[i - 1]] + 1)
        
        return dp[n][target] if dp[n][target] != -1 else -1