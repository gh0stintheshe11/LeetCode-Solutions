class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def area(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1)
        
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        points = set()
        sum_area = 0
        
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            sum_area += area(x1, y1, x2, y2)
            
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        
        if (min_x, min_y) not in points or (min_x, max_y) not in points or (max_x, min_y) not in points or (max_x, max_y) not in points or len(points) != 4:
            return False
        
        return sum_area == area(min_x, min_y, max_x, max_y)