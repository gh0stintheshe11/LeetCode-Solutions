from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        if k == 1:
            return sum(cost[0] for cost in costs)
        
        prev_min = prev_second_min = prev_min_index = 0
        
        for i in range(n):
            curr_min = curr_second_min = float('inf')
            curr_min_index = -1
            
            for j in range(k):
                cost = costs[i][j] + (prev_second_min if j == prev_min_index else prev_min)
                
                if cost < curr_min:
                    curr_second_min = curr_min
                    curr_min = cost
                    curr_min_index = j
                elif cost < curr_second_min:
                    curr_second_min = cost
            
            prev_min = curr_min
            prev_second_min = curr_second_min
            prev_min_index = curr_min_index
        
        return prev_min