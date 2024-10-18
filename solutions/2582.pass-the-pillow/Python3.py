class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Initial position of the pillow
        current_position = 1
        # Initial direction (1 means forward, -1 means backward)
        direction = 1
        
        for _ in range(time):
            # Move the pillow in the current direction
            current_position += direction
            
            # If the pillow reaches the end of the line, reverse the direction
            if current_position == n:
                direction = -1
            elif current_position == 1:
                direction = 1
        
        return current_position