class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Initialize the starting position
        x, y = 0, 0
        
        # Iterate through each move in the string
        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
        
        # Check if the robot is back at the origin
        return x == 0 and y == 0