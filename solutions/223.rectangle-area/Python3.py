class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate the area of both rectangles
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)
        
        # Calculate the overlap dimensions
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        
        # Calculate the overlap area
        overlap_area = overlap_width * overlap_height
        
        # Total area covered by both rectangles
        return areaA + areaB - overlap_area