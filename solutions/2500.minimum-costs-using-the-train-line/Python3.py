class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        regular_cost = 0
        express_cost = expressCost
        costs = []

        for i in range(n):
            next_regular_cost = min(regular_cost + regular[i], express_cost + express[i])
            next_express_cost = min(express_cost + express[i], regular_cost + regular[i] + expressCost)
            
            costs.append(next_regular_cost)
            regular_cost = next_regular_cost
            express_cost = next_express_cost

        return costs