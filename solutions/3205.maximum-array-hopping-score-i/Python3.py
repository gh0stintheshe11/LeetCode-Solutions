class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            max_score = float('-inf')
            for j in range(i + 1, n):
                max_score = max(max_score, (j - i) * nums[j] + dp[j])
            dp[i] = max_score
        
        return dp[0]