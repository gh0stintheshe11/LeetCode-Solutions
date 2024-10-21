class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> solutions;
        vector<string> board(n, string(n, '.'));
        vector<bool> cols(n, false), diag1(2 * n - 1, false), diag2(2 * n - 1, false);
        solve(0, n, board, solutions, cols, diag1, diag2);
        return solutions;
    }

private:
    void solve(int row, int n, vector<string>& board, vector<vector<string>>& solutions, 
               vector<bool>& cols, vector<bool>& diag1, vector<bool>& diag2) {
        if (row == n) {
            solutions.push_back(board);
            return;
        }
        for (int col = 0; col < n; ++col) {
            int d1 = row - col + n - 1;
            int d2 = row + col;
            if (!cols[col] && !diag1[d1] && !diag2[d2]) {
                board[row][col] = 'Q';
                cols[col] = diag1[d1] = diag2[d2] = true;
                solve(row + 1, n, board, solutions, cols, diag1, diag2);
                board[row][col] = '.';
                cols[col] = diag1[d1] = diag2[d2] = false;
            }
        }
    }
};