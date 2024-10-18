class Solution:
    def numberOfCleanRooms(self, room: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        visited_orientations = [[set() for _ in range(len(room[0]))] for _ in range(len(room))]
        
        x, y, dir_index = 0, 0, 0
        cleaned_spaces = set()
        
        while (x, y, dir_index) not in visited_orientations[x][y]:
            visited_orientations[x][y].add((x, y, dir_index))
            cleaned_spaces.add((x, y))
            
            dx, dy = directions[dir_index]
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < len(room) and 0 <= new_y < len(room[0]) and room[new_x][new_y] == 0:
                x, y = new_x, new_y
            else:
                dir_index = (dir_index + 1) % 4

        return len(cleaned_spaces)