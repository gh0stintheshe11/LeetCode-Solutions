from typing import List

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        
        if n < 3:
            return -1
        
        # This will store the left max profit that corresponds to the condition
        left_max = [0] * n
        max_profit = -1

        # Find the max profit where j is the middle element
        for j in range(n):
            left_best = 0
            right_best = 0
            
            # For each j, find the maximum available left profit with condition
            for i in range(j):
                if prices[i] < prices[j]:
                    left_best = max(left_best, profits[i])
            left_max[j] = left_best

            # For each j, find the maximum available right profit with condition
            for k in range(j + 1, n):
                if prices[j] < prices[k]:
                    right_best = max(right_best, profits[k])

            # If we have valid left and right, calculate the max profit
            if left_max[j] > 0 and right_best > 0:
                max_profit = max(max_profit, left_max[j] + profits[j] + right_best)

        return max_profit if max_profit != -1 else -1