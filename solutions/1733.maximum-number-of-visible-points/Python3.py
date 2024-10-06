from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        same_location_count = 0
        angles = []
        
        # Calculate angles and count points at the same location
        for x, y in points:
            if x == x0 and y == y0:
                same_location_count += 1
            else:
                angle_rad = math.atan2(y - y0, x - x0)
                angles.append(math.degrees(angle_rad))
        
        # Sort angles
        angles.sort()
        
        # Create a circular list by adding 360 to each angle
        angles += [a + 360 for a in angles]
        
        # Find maximum number of points in a window defined by the given angle
        max_visible = 0
        left = 0
        angle = float(angle)  # convert to float to account for angle calculations
        
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)
        
        return max_visible + same_location_count