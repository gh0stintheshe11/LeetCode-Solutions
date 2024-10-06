class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        queen_set = set(map(tuple, queens))
        result = []
        
        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if (x, y) in queen_set:
                    result.append([x, y])
                    break
        
        return result