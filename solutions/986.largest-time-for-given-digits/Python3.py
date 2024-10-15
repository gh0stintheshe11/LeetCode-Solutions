from itertools import permutations
from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        
        # Permute all the possible times
        for perm in permutations(arr):
            # Use tuples to convert to HH:MM
            h1, h2, m1, m2 = perm
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            
            # Check if valid time
            if hours < 24 and minutes < 60:
                total_minutes = hours * 60 + minutes
                if total_minutes > max_time:
                    max_time = total_minutes
                    max_time_str = f"{h1}{h2}:{m1}{m2}"
        
        return max_time_str if max_time != -1 else ""