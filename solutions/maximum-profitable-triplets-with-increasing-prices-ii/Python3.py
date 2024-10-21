from sortedcontainers import SortedList
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        def leftsolve(prices, profits):
            n = len(prices)
            sl = SortedList([(float('-inf'), float('-inf'))])
            left = [0] * n
            for i, p in enumerate(prices):
                j = sl.bisect_left((p, profits[i]))
                while j < len(sl) and profits[i] >= sl[j][1]:
                    sl.pop(j)
                if profits[i] > sl[j-1][1]:
                    sl.add((p, profits[i]))
                j = sl.bisect_left((p, float('-inf')))
                left[i] = sl[j-1][1]
            return left

        def rightsolve(prices, profits):
            n = len(prices)
            sl = SortedList([(float('inf'), float('-inf'))])
            right = [0] * n
            for i in range(n-1, -1, -1):
                p = prices[i]
                j = sl.bisect_right((p, profits[i]))
                while j > 0 and profits[i] >= sl[j-1][1]:
                    sl.pop(j-1)
                    j = sl.bisect_right((p, profits[i]))
                if profits[i] > sl[j][1]:
                    sl.add((p, profits[i]))
                j = sl.bisect_right((p, float('inf')))
                right[i] = sl[j][1]
            return right

        left = leftsolve(prices, profits)
        right = rightsolve(prices, profits)
        res = float('-inf')
        for i in range(len(prices)):
            res = max(res, profits[i] + left[i] + right[i])
        return res if res != float('-inf') else -1