class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        
        for x, y, r in circles:
            for dx in range(-r, r + 1):
                for dy in range(-r, r + 1):
                    if dx * dx + dy * dy <= r * r:
                        points.add((x + dx, y + dy))
        
        return len(points)