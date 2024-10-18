class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # Initialize starting position
        row, col = 0, 0
        # Direction map for each command
        direction = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        
        # Process each command
        for command in commands:
            dr, dc = direction[command]
            row += dr
            col += dc
        
        # Calculate final position in array cell format
        return row * n + col