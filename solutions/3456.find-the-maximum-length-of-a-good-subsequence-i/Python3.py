class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [[0] * (k + 1) for _ in range(N + 1)]
        max_len = 0
        for i in reversed(range(N)):
            for g in range(k + 1):
                res = 1
                for j in range(i + 1, N):
                    if nums[i] == nums[j]:
                        res = max(res, 1 + dp[j][g])
                    elif g + 1 <= k:
                        res = max(res, 1 + dp[j][g + 1])
                dp[i][g] = res
                max_len = max(max_len, dp[i][g])
        return max_len