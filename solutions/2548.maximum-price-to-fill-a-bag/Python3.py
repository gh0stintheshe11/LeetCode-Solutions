from typing import List

class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        # Calculate price per unit weight for each item
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        total_value = 0.0
        current_weight = 0
        
        for price, weight in items:
            if current_weight >= capacity:
                break
            if current_weight + weight <= capacity:
                total_value += price
                current_weight += weight
            else:
                remaining_capacity = capacity - current_weight
                total_value += (price / weight) * remaining_capacity
                current_weight = capacity

        return total_value if current_weight == capacity else -1.0