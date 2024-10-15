class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = 0
        best_coord = [0, 0]
        radius_squared = radius * radius
        
        for x in range(51):
            for y in range(51):
                quality = 0
                for tx, ty, q in towers:
                    dx, dy = x - tx, y - ty
                    distance_squared = dx * dx + dy * dy
                    if distance_squared <= radius_squared:
                        distance = math.sqrt(distance_squared)
                        quality += int(q / (1 + distance))
                
                if quality > max_quality or (quality == max_quality and [x, y] < best_coord):
                    max_quality = quality
                    best_coord = [x, y]
        
        return best_coord