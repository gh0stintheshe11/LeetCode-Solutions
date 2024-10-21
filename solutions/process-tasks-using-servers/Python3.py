from heapq import heappop, heappush
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available_servers)
        busy_servers = []
        result = []
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            current_time = max(current_time, j)
            
            while busy_servers and busy_servers[0][0] <= current_time:
                _, w, i = heappop(busy_servers)
                heappush(available_servers, (w, i))
            
            if available_servers:
                w, i = heappop(available_servers)
                heappush(busy_servers, (current_time + task_time, w, i))
                result.append(i)
            else:
                busy_until, w, i = heappop(busy_servers)
                current_time = busy_until
                heappush(busy_servers, (current_time + task_time, w, i))
                result.append(i)
        
        return result