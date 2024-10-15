class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for s in dp[:]:
                dp[(s + num) % 3] = max(dp[(s + num) % 3], s + num)
        return dp[0]