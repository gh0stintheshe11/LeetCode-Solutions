from collections import deque
import functools
import math
from typing import List

class Solution:
    @functools.cache
    def get_moves(self, kx, ky, x, y):
        """This function finds minimum moves to capture pawn at position from kx, ky"""
        q = deque()
        q.append((kx, ky, 0))
        visited = set()
        while q:
            for _ in range(len(q)):
                cx, cy, moves = q.popleft()
                if cx == x and cy == y:
                    return moves
                # 8 possible directions for the knight
                directions = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
                for dx, dy in directions:
                    if 0 <= cx + dx < 50 and 0 <= cy + dy < 50 and (cx + dx, cy + dy) not in visited:
                        q.append((cx + dx, cy + dy, moves + 1))
                        visited.add((cx + dx, cy + dy))
                        
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:

        @functools.cache
        def dfs(kx, ky, pawns, aliceTurn):

            if pawns == (1 << len(positions)) - 1:
                return 0  # No more moves to make

            func = max if aliceTurn else min
            ans = -math.inf if aliceTurn else math.inf
            for i in range(len(positions)):
                curr_mask = 1 << i
                if pawns & curr_mask:
                    # If already captured
                    continue
                nx, ny = positions[i]
                min_moves = self.get_moves(kx, ky, nx, ny)
                ans = func(ans, min_moves + dfs(nx, ny, pawns | curr_mask, 1 - aliceTurn))

            return ans
        
        return dfs(kx, ky, 0, 1)