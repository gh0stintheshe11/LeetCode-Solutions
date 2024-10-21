class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int m = board.size();
        int n = board[0].size();
        int x = click[0], y = click[1];

        if (board[x][y] == 'M') {
            board[x][y] = 'X';
        } else {
            reveal(board, x, y, m, n);
        }

        return board;
    }

private:
    void reveal(vector<vector<char>>& board, int x, int y, int m, int n) {
        if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] != 'E') return;

        int mines = countMines(board, x, y, m, n);
        if (mines > 0) {
            board[x][y] = '0' + mines;
        } else {
            board[x][y] = 'B';
            for (int dx = -1; dx <= 1; ++dx) {
                for (int dy = -1; dy <= 1; ++dy) {
                    if (dx != 0 || dy != 0) {
                        reveal(board, x + dx, y + dy, m, n);
                    }
                }
            }
        }
    }

    int countMines(vector<vector<char>>& board, int x, int y, int m, int n) {
        int mines = 0;
        for (int dx = -1; dx <= 1; ++dx) {
            for (int dy = -1; dy <= 1; ++dy) {
                if (dx != 0 || dy != 0) {
                    int nx = x + dx, ny = y + dy;
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == 'M') {
                        ++mines;
                    }
                }
            }
        }
        return mines;
    }
};