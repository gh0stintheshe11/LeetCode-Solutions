import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        stations.append([target, 0])
        fuel = startFuel
        stops = 0
        prev = 0
        
        for pos, gas in stations:
            fuel -= pos - prev
            while max_heap and fuel < 0:
                fuel += -heapq.heappop(max_heap)
                stops += 1
            if fuel < 0:
                return -1
            heapq.heappush(max_heap, -gas)
            prev = pos
        
        return stops