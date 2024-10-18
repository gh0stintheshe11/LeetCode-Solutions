class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(2, n + 1):
            if nums[i - 1] == nums[i - 2] and dp[i - 2]:
                dp[i] = True
            if i > 2 and nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3]:
                dp[i] = True
            if i > 2 and nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2 and dp[i - 3]:
                dp[i] = True
        
        return dp[n]