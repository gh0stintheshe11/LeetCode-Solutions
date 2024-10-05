from typing import List
import collections

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert stickers to a list of counts of characters
        sticker_counts = [collections.Counter(sticker) for sticker in stickers]
        dp = {}
        dp[""] = 0

        def dfs(t):
            if t in dp:
                return dp[t]
            # Initial value for min_cost is a very large number
            min_cost = float('inf')
            target_count = collections.Counter(t)
            for sticker in sticker_counts:
                if sticker[t[0]] == 0: 
                    continue  # optimization: skip invalid stickers
                # Construct a new target after using this sticker
                new_target = []
                for char in target_count:
                    if target_count[char] > sticker[char]:
                        new_target.append(char * (target_count[char] - sticker[char]))
                new_target = "".join(new_target)
                attempt = dfs(new_target)
                if attempt != -1:
                    min_cost = min(min_cost, 1 + attempt)
            # Update dp dictionary
            dp[t] = -1 if min_cost == float('inf') else min_cost
            return dp[t]

        # Start the DFS from the target
        result = dfs(target)
        return result