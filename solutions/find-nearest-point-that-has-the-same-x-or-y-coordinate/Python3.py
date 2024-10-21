class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        result_index = -1

        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                distance = abs(px - x) + abs(py - y)

                if distance < min_distance:
                    min_distance = distance
                    result_index = i

        return result_index