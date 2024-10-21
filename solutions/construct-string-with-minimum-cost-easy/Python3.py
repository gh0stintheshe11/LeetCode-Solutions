from typing import List

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        # Initialize dp array with infinity except dp[0] = 0 (base case)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Check each position 'i' in target
        for i in range(n):
            # If we can't reach position 'i', continue
            if dp[i] == float('inf'):
                continue
            # Try to match each word at position 'i'
            for j, word in enumerate(words):
                L = len(word)
                if i + L <= n and target[i:i+L] == word:
                    dp[i + L] = min(dp[i + L], dp[i] + costs[j])
        
        return dp[n] if dp[n] != float('inf') else -1