class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        def is_valid_move(x, y):
            return 0 <= x < m and 0 <= y < n and board[x][y] == -1
        
        def knight_tour(x, y, move_count):
            if move_count == m * n:
                return True
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if is_valid_move(nx, ny):
                    board[nx][ny] = move_count
                    if knight_tour(nx, ny, move_count + 1):
                        return True
                    board[nx][ny] = -1
            return False
        
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        board = [[-1 for _ in range(n)] for _ in range(m)]
        board[r][c] = 0
        
        knight_tour(r, c, 1)
        
        return board