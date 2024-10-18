class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            max_length = 0
            for i in range(max(0, index - k), min(25, index + k) + 1):
                max_length = max(max_length, dp[i])
            dp[index] = max_length + 1
        return max(dp)