from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_cost = float('inf')
        
        # Prefix sum to track min cost to collect chocolates
        prefix_min_cost = [float('inf')] * n
        for k in range(n):
            total_operations_cost = k * x
            for i in range(n):
                # Update the minimum cost to collect chocolate of type i
                prefix_min_cost[i] = min(prefix_min_cost[i], nums[(i - k) % n])
                
            # Calculate total cost for k rotations
            total_cost = total_operations_cost + sum(prefix_min_cost)
            min_cost = min(min_cost, total_cost)
        
        return min_cost