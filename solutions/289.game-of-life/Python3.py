class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def count_neighbors(row, col):
            directions = [(-1, -1), (-1, 0), (-1, 1), 
                          (0, -1),         (0, 1), 
                          (1, -1), (1, 0), (1, 1)]
            count = 0
            for dx, dy in directions:
                r, c = row + dx, col + dy
                if 0 <= r < m and 0 <= c < n and (board[r][c] in [1, 3]):
                    count += 1
            return count

        for i in range(m):
            for j in range(n):
                live_neighbors = count_neighbors(i, j)
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 3 # live to dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2 # dead to live

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0