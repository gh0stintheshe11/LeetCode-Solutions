class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        
        for cost in costs:
            count[cost] += 1
        
        num_ice_cream = 0
        
        for price in range(1, max_cost + 1):
            if coins < price:
                break
            if count[price] > 0:
                buy = min(count[price], coins // price)
                num_ice_cream += buy
                coins -= buy * price
        
        return num_ice_cream