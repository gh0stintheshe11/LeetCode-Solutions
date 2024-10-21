class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10**9 + 7
        n = len(pressedKeys)

        # DP array to store the number of possible messages up to each index
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to decode an empty string

        def valid_length(key, length):
            if key in {'7', '9'}:
                return length <= 4
            else:
                return length <= 3

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # Single character mapping
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] = (dp[i] + dp[i - 2]) % mod
            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
                dp[i] = (dp[i] + dp[i - 3]) % mod
            if i >= 4 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3] == pressedKeys[i - 4] and valid_length(pressedKeys[i - 1], 4):
                dp[i] = (dp[i] + dp[i - 4]) % mod

        return dp[n]