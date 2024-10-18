class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k, -1, -1):
                if is_palindrome(s[j:i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
                    
        return dp[n]