from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def dfs(i, current_cost):
            nonlocal closest
            
            if i == len(toppingCosts):
                if abs(current_cost - target) < abs(closest - target) or \
                   (abs(current_cost - target) == abs(closest - target) and current_cost < closest):
                    closest = current_cost
                return

            # Use no topping of this type
            dfs(i + 1, current_cost)
            # Use one topping of this type
            dfs(i + 1, current_cost + toppingCosts[i])
            # Use two toppings of this type
            dfs(i + 1, current_cost + 2 * toppingCosts[i])
        
        closest = float('inf')
        for base in baseCosts:
            dfs(0, base)
        
        return closest