from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        
        max_time = 0
        for i in range(len(processorTime)):
            max_time = max(max_time, processorTime[i] + max(tasks[i * 4: (i + 1) * 4]))
        
        return max_time