from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Process each row to simulate gravity
        for row in box:
            write_pos = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    write_pos = col - 1
                elif row[col] == '#':
                    if write_pos != col:
                        row[write_pos], row[col] = row[col], row[write_pos]
                    write_pos -= 1
        
        # Rotate the box 90 degrees clockwise
        rotated_box = [[''] * m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                rotated_box[col][m - row - 1] = box[row][col]
        
        return rotated_box