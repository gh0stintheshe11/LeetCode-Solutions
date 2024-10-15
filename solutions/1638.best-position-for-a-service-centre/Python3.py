import math
from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def total_distance(x: float, y: float) -> float:
            return sum(math.sqrt((p[0] - x) ** 2 + (p[1] - y) ** 2) for p in positions)

        # We will utilize gradient descent to find the optimal point
        x0, y0 = 50.0, 50.0  # Start from the middle of the given range
        best_dist = total_distance(x0, y0)
        step = 1.0
        precision = 1e-7

        while step > precision:
            found_better = False
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x0 + step * dx, y0 + step * dy
                dist = total_distance(nx, ny)
                if dist < best_dist:
                    best_dist = dist
                    x0, y0 = nx, ny
                    found_better = True
                    break
            if not found_better:
                step /= 2.0

        return best_dist