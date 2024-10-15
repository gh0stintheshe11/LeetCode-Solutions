from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        m = len(s)
        result = [0] * m
        
        for i in range(m):
            x, y = startPos
            count = 0
            for j in range(i, m):
                dx, dy = directions[s[j]]
                x += dx
                y += dy
                if 0 <= x < n and 0 <= y < n:
                    count += 1
                else:
                    break
            result[i] = count
        
        return result