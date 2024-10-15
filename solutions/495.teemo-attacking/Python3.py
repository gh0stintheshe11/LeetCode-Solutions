from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_poisoned_time = 0
        for i in range(1, len(timeSeries)):
            total_poisoned_time += min(timeSeries[i] - timeSeries[i-1], duration)
        
        total_poisoned_time += duration
        return total_poisoned_time