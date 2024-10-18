class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        remaining_capacity = [capacity[i] - rocks[i] for i in range(n)]
        
        remaining_capacity.sort()
        
        filled_bags = 0
        for space_needed in remaining_capacity:
            if additionalRocks >= space_needed:
                additionalRocks -= space_needed
                filled_bags += 1
            else:
                break
        
        return filled_bags