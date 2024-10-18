class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def calculate_costs(node: int) -> int:
            if node > n:
                return 0
            left = calculate_costs(2 * node)
            right = calculate_costs(2 * node + 1)
            nonlocal increments
            increments += abs(left - right)
            return cost[node - 1] + max(left, right)
        
        increments = 0
        calculate_costs(1)
        return increments