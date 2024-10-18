class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Initial position and direction
        x, y = 0, 0
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Start facing North
        direction_index = 0
        
        for instruction in instructions:
            if instruction == 'G':
                x += directions[direction_index][0]
                y += directions[direction_index][1]
            elif instruction == 'L':
                direction_index = (direction_index + 3) % 4  # Turn left
            elif instruction == 'R':
                direction_index = (direction_index + 1) % 4  # Turn right
        
        # Check if the robot is back at the origin or not facing north
        return (x == 0 and y == 0) or (direction_index != 0)
