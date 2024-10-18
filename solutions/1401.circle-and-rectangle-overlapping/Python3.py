class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point on the rectangle to the circle's center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the distance between the circle's center and this closest point
        distanceX = xCenter - closestX
        distanceY = yCenter - closestY
        
        # If the distance is less than or equal to the radius, they overlap
        return distanceX**2 + distanceY**2 <= radius**2