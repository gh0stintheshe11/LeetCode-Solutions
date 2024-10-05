from typing import List
import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        
        # Create a list of distances with worker, bike and their distances and then sort them based on the problem requirements
        distances = []
        for i in range(n):
            for j in range(m):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                distances.append((dist, i, j))
        
        # Sorting distances by distance first, then by worker index, then by bike index
        distances.sort()
        
        result = [-1] * n
        bike_taken = [False] * m
        worker_assigned = [False] * n
        
        count = 0
        for dist, w, b in distances:
            if not worker_assigned[w] and not bike_taken[b]:
                result[w] = b
                bike_taken[b] = True
                worker_assigned[w] = True
                count += 1
                if count == n:
                    break
        
        return result