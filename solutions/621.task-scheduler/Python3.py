from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while max_heap:
            i, temp = 0, []
            while i <= n:
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    if cnt < -1:
                        temp.append(cnt + 1)
                time += 1
                if not max_heap and not temp:
                    break
                i += 1
            for item in temp:
                heapq.heappush(max_heap, item)
        
        return time