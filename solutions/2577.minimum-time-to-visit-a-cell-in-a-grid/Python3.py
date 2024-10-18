from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = []
        if grid[0][0] or (grid[1][0] > grid[0][0] + 1 and grid[0][1] > grid[0][0] + 1):
            return -1

        heappush(minHeap, (0, (0, 0)))
        m = len(grid) - 1
        n = len(grid[0]) - 1

        while minHeap:
            time_till_position, (i, j) = heappop(minHeap)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if (i, j) == (m, n):
                return time_till_position

            for neighbour_i, neighbour_j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= neighbour_i <= m and 0 <= neighbour_j <= n and (neighbour_i, neighbour_j) not in visited:
                    time_to_reach_neighbour = time_till_position + 1
                    time_limit_at_neighbour = grid[neighbour_i][neighbour_j]

                    if time_to_reach_neighbour >= time_limit_at_neighbour:
                        heappush(minHeap, (time_to_reach_neighbour, (neighbour_i, neighbour_j)))
                    else:
                        heappush(minHeap, (time_limit_at_neighbour + (time_limit_at_neighbour - time_to_reach_neighbour) % 2, (neighbour_i, neighbour_j)))