from collections import defaultdict, deque
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].popleft())
            itinerary.appendleft(airport)
        
        graph = defaultdict(deque)
        for src, dst in sorted(tickets):
            graph[src].append(dst)
        
        itinerary = deque()
        dfs("JFK")
        
        return list(itinerary)