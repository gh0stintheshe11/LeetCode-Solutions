class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        def capture_pawns(x, y):
            captures = 0
            for dx, dy in directions:
                nx, ny = x, y
                while 0 <= nx < 8 and 0 <= ny < 8:
                    if board[nx][ny] == 'B': 
                        break
                    if board[nx][ny] == 'p':
                        captures += 1
                        break
                    nx += dx
                    ny += dy
            return captures
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return capture_pawns(i, j)