class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 0
        for num in arr:
            prev = num - difference
            dp[num] = dp.get(prev, 0) + 1
            max_length = max(max_length, dp[num])
        return max_length