from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        # Calculate the maximum overlap between two strings a and b
        def find_overlap(a: str, b: str) -> int:
            # Max overlap is the start of b matching the end of a
            for i in range(min(len(a), len(b)), 0, -1):
                if a[-i:] == b[:i]:
                    return i
            return 0

        # Precompute overlaps
        overlaps = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    overlaps[i][j] = find_overlap(words[i], words[j])

        # DP array to store the shortest superstring length using all words in mask
        dp = [[''] * n for _ in range(1 << n)]

        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    # If i-th bit is set in mask (i.e., words[i] is in the current subset)
                    if mask == (1 << i):
                        # If the mask has only one bit set, just place the word itself
                        dp[mask][i] = words[i]
                    else:
                        # Try to add words[i] to the superstring formed by removing words[i] from 'mask'
                        for j in range(n):
                            if mask & (1 << j) and i != j:
                                # j is in the mask and j is not i
                                candidate = dp[mask ^ (1 << i)][j] + words[i][overlaps[j][i]:]
                                if dp[mask][i] == '' or len(dp[mask][i]) > len(candidate):
                                    dp[mask][i] = candidate
        
        # Find the superstring with minimum length that includes all words
        min_superstring = ''
        final_mask = (1 << n) - 1
        for i in range(n):
            if min_superstring == '' or len(dp[final_mask][i]) < len(min_superstring):
                min_superstring = dp[final_mask][i]
        
        return min_superstring