class Solution:
    def maxScore(self, prices: List[int]) -> int:
        from collections import defaultdict
        
        # Create a dictionary to store the sum of prices that belong to the same group
        group_sum = defaultdict(int)
        
        # Calculate the group key and accumulate the values
        for i, price in enumerate(prices):
            group_key = price - (i + 1)
            group_sum[group_key] += price
        
        # Return the maximum sum among all groups
        return max(group_sum.values())