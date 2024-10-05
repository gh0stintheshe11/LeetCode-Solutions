class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        point_set = set((x, y) for x, y in points)
        min_x = min(x for x, y in point_set)
        max_x = max(x for x, y in point_set)
        reflection_line = (min_x + max_x) / 2

        for x, y in point_set:
            if (int(reflection_line * 2) - x, y) not in point_set:
                return False
        return True