from typing import List

class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        from itertools import combinations

        max_dist = 0

        # Calculate manhattan distance between each pair of points
        for p1, p2 in combinations(points, 2):
            dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            max_dist = max(max_dist, dist)

        # Binary search over distances
        left, right = 0, max_dist
        while left < right:
            mid = (left + right) // 2
            if self.canHaveKVariants(points, k, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canHaveKVariants(self, points: List[List[int]], k: int, days: int) -> bool:
        cover = set()

        # Generate coverage area for each point
        for x, y in points:
            for dx in range(-days, days + 1):
                for dy in range(-days + abs(dx), days - abs(dx) + 1):
                    cover.add((x + dx, y + dy))

        # We need at least k points in the coverage
        for point in cover:
            count = sum(1 for x, y in points if abs(x - point[0]) + abs(y - point[1]) <= days)
            if count >= k:
                return True

        return False