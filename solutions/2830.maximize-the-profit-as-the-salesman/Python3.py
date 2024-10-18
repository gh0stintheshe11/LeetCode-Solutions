from typing import List

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)
        offer_idx = 0
        m = len(offers)

        for i in range(n):
            # Carry over the maximum value up to the current house
            if i > 0:
                dp[i] = max(dp[i], dp[i-1])
            
            # Update the dp value based on current offers
            while offer_idx < m and offers[offer_idx][1] == i:
                start, end, gold = offers[offer_idx]
                dp[end] = max(dp[end], (dp[start - 1] if start > 0 else 0) + gold)
                offer_idx += 1

        return max(dp)