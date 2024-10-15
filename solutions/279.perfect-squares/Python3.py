import math
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        level = 0
        queue = deque([n])
        while queue:
            level += 1
            next_queue = deque()
            for remainder in queue:
                for square in squares:
                    if remainder == square:
                        return level
                    if remainder < square:
                        break
                    next_queue.append(remainder - square)
            queue = next_queue
        return level