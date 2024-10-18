from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def canProduce(machine: List[int], num_alloys: int) -> bool:
            total_cost = 0
            for j in range(n):
                required = num_alloys * machine[j]
                if required > stock[j]:
                    total_cost += (required - stock[j]) * cost[j]
                if total_cost > budget:
                    return False
            return True

        max_alloys = 0
        for machines in composition:
            left, right = 0, 10**9  # using a larger value for right boundary
            
            while left < right:
                mid = (left + right + 1) // 2
                if canProduce(machines, mid):
                    left = mid
                else:
                    right = mid - 1
            
            max_alloys = max(max_alloys, left)
        
        return max_alloys