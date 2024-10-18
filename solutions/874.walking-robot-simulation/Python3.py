class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions are in the order of North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0  # Starts facing north
        x, y = 0, 0
        max_distance = 0
        obstacle_set = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                dir_index = (dir_index - 1) % 4
            elif cmd == -1:  # Turn right
                dir_index = (dir_index + 1) % 4
            else:
                for _ in range(cmd):
                    next_x = x + dirs[dir_index][0]
                    next_y = y + dirs[dir_index][1]
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance = max(max_distance, x * x + y * y)
                    else:
                        break
        
        return max_distance