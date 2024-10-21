from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Combine plantTime and growTime into pairs
        seeds = list(zip(growTime, plantTime))
        
        # Sort seeds by growTime in descending order
        seeds.sort(reverse=True, key=lambda x: x[0])
        
        # Variables to track the current planting day and bloom time
        current_planting_day = 0
        max_bloom_day = 0
        
        # Process each seed
        for grow, plant in seeds:
            # Accumulate planting days
            current_planting_day += plant
            # Calculate the bloom day for this seed
            bloom_day = current_planting_day + grow
            # Track the maximum bloom day seen
            max_bloom_day = max(max_bloom_day, bloom_day)
        
        return max_bloom_day