from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort the costs based on the difference between cost to city A and cost to city B
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total_cost = 0
        
        # Send first n people to city A and rest to city B
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]
        
        return total_cost