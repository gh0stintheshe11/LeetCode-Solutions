from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [i for i in range(n + 1)]
        
        for i in range(1, n + 1):
            for word in dictionary:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word:
                    dp[i] = min(dp[i], dp[i - word_len])
            dp[i] = min(dp[i], dp[i - 1] + 1)
        
        return dp[n]
