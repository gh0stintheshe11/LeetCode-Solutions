from typing import List

class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        it_indices = [i for i, x in enumerate(team) if x == 1]
        non_it_indices = [i for i, x in enumerate(team) if x == 0]
        
        i, j = 0, 0
        caught_count = 0
        
        while i < len(it_indices) and j < len(non_it_indices):
            if abs(it_indices[i] - non_it_indices[j]) <= dist:
                caught_count += 1
                i += 1
                j += 1
            elif it_indices[i] < non_it_indices[j]:
                i += 1
            else:
                j += 1
                
        return caught_count