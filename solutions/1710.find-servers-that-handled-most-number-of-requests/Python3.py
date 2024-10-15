from typing import List
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available_servers = SortedList(range(k))
        server_tasks = []
        request_count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Release all servers that have finished their tasks by the current arrival time
            while server_tasks and server_tasks[0][0] <= start:
                end_time, server_index = heapq.heappop(server_tasks)
                available_servers.add(server_index)

            if available_servers:
                # Find the first available server >= i % k
                idx = available_servers.bisect_left(i % k)
                if idx == len(available_servers):
                    idx = 0
                selected_server = available_servers[idx]
                available_servers.remove(selected_server)

                # Queue the server with its end time
                heapq.heappush(server_tasks, (start + duration, selected_server))
                request_count[selected_server] += 1

        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]