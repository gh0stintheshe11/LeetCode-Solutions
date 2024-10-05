from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by their lengths
        words.sort(key=len)
        
        # Dictionary to store the longest chain ending at each word
        dp = {}
        
        # Variable to keep track of the longest chain found
        longest_chain = 1
        
        for word in words:
            dp[word] = 1  # Each word is a chain of at least length 1
            # Try removing each character from the word
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            # Update the longest chain found
            longest_chain = max(longest_chain, dp[word])
        
        return longest_chain
