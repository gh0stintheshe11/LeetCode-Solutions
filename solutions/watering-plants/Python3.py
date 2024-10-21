from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        
        for i, water_needed in enumerate(plants):
            if water_needed > current_water:
                steps += i * 2
                current_water = capacity
            
            steps += 1
            current_water -= water_needed
        
        return steps