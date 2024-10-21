from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for numPassengers, start, end in trips:
            events.append((start, numPassengers))
            events.append((end, -numPassengers))
        
        events.sort()
        
        current_capacity = 0
        for event in events:
            current_capacity += event[1]
            if current_capacity > capacity:
                return False
        
        return True