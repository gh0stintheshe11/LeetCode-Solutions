class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        # Sort points based on x-coordinate
        points.sort(key=lambda x: x[0])
        
        n = len(points)
        rectangles = 0
        i = 0
        
        while i < n:
            # Start with the smallest x-coordinate in the remaining points
            rectangles += 1
            # Define the range this rectangle can cover
            cover_end = points[i][0] + w
            # Move i past all points covered by this rectangle
            while i < n and points[i][0] <= cover_end:
                i += 1
        
        return rectangles