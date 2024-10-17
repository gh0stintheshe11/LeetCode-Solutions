from typing import Optional
from functools import lru_cache
from collections import deque

class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        N, M = len(grid), len(grid[0])
        mouse_pos = None
        cat_pos = None
        food_pos = None
        _grid = [list(row) for row in grid]

        for i in range(N):
            for j in range(M):
                if _grid[i][j] == "C":
                    cat_pos = (i, j)
                    _grid[i][j] = "."
                elif _grid[i][j] == "M":
                    mouse_pos = (i, j)
                    _grid[i][j] = "."
                elif _grid[i][j] == "F":
                    food_pos = (i, j)
                    _grid[i][j] = "."

        assert mouse_pos is not None
        assert cat_pos is not None
        assert food_pos is not None

        def next_positions(pos, max_jump):
            i, j = pos
            # UP
            for k in range(1, max_jump + 1):
                if i + k >= N or _grid[i + k][j] == "#":
                    break
                yield (i + k, j)
            # RIGHT
            for k in range(1, max_jump + 1):
                if j + k >= M or _grid[i][j + k] == "#":
                    break
                yield (i, j + k)
            # DOWN
            for k in range(1, max_jump + 1):
                if i - k < 0 or _grid[i - k][j] == "#":
                    break
                yield (i - k, j)
            # RIGHT
            for k in range(1, max_jump + 1):
                if j - k < 0 or _grid[i][j - k] == "#":
                    break
                yield (i, j - k)
            # Stay still
            yield (i, j)

        # Calculate distance to food
        distance_to_food = dict[tuple[int, int], int]()
        queue = deque[tuple[int, int, int]]()
        queue.append((0, *food_pos))

        while queue:
            distance, i, j = queue.pop()

            if (i, j) in distance_to_food:
                if distance < distance_to_food[(i, j)]:
                    distance_to_food[(i, j)] = distance
                continue
            
            distance_to_food[(i, j)] = distance

            for ni, nj in next_positions((i, j), max_jump=1):
                queue.append((distance + 1, ni, nj))
            
            
        @lru_cache(maxsize=None)
        def mouse_wins(turn: int, mouse_pos: tuple[int, int], cat_pos: tuple[int, int]) -> bool:
            if turn == 1000 or turn == 2 * N * M: # Early stopping
                return False
            if mouse_pos == cat_pos:
                return False
            if mouse_pos == food_pos:
                return True
            if cat_pos == food_pos:
                return False

            if turn % 2 == 0: # Mouse turn
                # Get pos sorted by distance to food
                # If not reachable, set all to 0 (no sort)
                positions = sorted(
                    next_positions(mouse_pos, mouseJump), 
                    key=lambda p: distance_to_food.get(p, 0)
                )
                # Min max
                for next_pos in positions:
                    if mouse_wins(turn + 1, next_pos, cat_pos):
                        return True
                # Else, mouse loses
                return False
            else: # Cat turn
                # Get pos sorted by distance to food
                # If not reachable, set all to 0 (no sort)
                positions = sorted(
                    next_positions(cat_pos, catJump),
                    key=lambda p: distance_to_food.get(p, 0)
                )
                # Min max
                for next_pos in positions:
                    if not mouse_wins(turn + 1, mouse_pos, next_pos):
                        return False
                # Else, mouse wins
                return True
        
        # Early stopping
        if mouse_pos not in distance_to_food:
            return False
        if cat_pos not in distance_to_food:
            return True
        
        return mouse_wins(0, mouse_pos, cat_pos)