class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the angle of the minute hand
        minute_angle = minutes * 6
        
        # Calculate the angle of the hour hand
        hour_angle = (hour % 12) * 30 + (minutes / 60) * 30
        
        # Find the difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller angle between the two possible options
        return min(angle, 360 - angle)