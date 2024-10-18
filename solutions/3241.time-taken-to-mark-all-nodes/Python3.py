from collections import defaultdict
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list) 
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        dp = [defaultdict(int) for _ in range(len(graph))]
        already = [[0, 0] for _ in range(len(graph))]
        visited, times = set(), [0] * len(graph)

        def find(node: int = 0) -> int:
            visited.add(node)
            maxTime = secondMaxTime = 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    time = find(neighbor) + (1 if neighbor & 1 else 2)
                    dp[node][neighbor] = time
                    if time >= maxTime:
                        secondMaxTime = maxTime
                        maxTime = time
                    elif time > secondMaxTime:
                        secondMaxTime = time
            already[node] = [maxTime, secondMaxTime]
            return maxTime

        times[0] = find()
        for node in range(1, len(graph)):
            maxTime = 0
            for neighbor in graph[node]:
                time, tempMaxTime = (1 if neighbor & 1 else 2), 0
                max1, max2 = already[neighbor]
                tempMaxTime = (max2 if dp[neighbor][node] == max1 else max1)
                maxTime = max(maxTime, tempMaxTime + time)
                if dp[node][neighbor] != tempMaxTime + time:
                    if tempMaxTime + time >= already[node][0]:
                        already[node][1] = already[node][0]
                        already[node][0] = tempMaxTime + time
                    elif tempMaxTime + time >= already[node][1]:
                        already[node][1] = tempMaxTime + time
                dp[node][neighbor] = tempMaxTime + time
            times[node] = maxTime
        return times