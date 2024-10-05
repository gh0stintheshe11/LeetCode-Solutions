from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}
        for row in wall:
            edge = 0
            for brick in row[:-1]:
                edge += brick
                if edge in edges:
                    edges[edge] += 1
                else:
                    edges[edge] = 1

        max_edges = max(edges.values(), default=0)
        return len(wall) - max_edges