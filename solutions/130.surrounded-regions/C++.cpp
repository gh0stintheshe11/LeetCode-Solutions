class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        int m = board.size();
        int n = board[0].size();

        function<void(int, int)> dfs = [&](int i, int j) {
            if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') return;
            board[i][j] = '#';
            dfs(i + 1, j);
            dfs(i - 1, j);
            dfs(i, j + 1);
            dfs(i, j - 1);
        };

        // Start from the first and last row
        for (int i = 0; i < m; ++i) {
            dfs(i, 0);
            dfs(i, n - 1);
        }

        // Start from the first and last column
        for (int j = 0; j < n; ++j) {
            dfs(0, j);
            dfs(m - 1, j);
        }

        // Traverse the board and convert 'O' to 'X' and '#' back to 'O'
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }
};