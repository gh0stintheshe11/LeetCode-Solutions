class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        for num in nums:
            rem = num % k
            for i in range(k):
                dp[i][rem] = dp[i][(i-rem) % k] + 1
        return max(max(row) for row in dp)