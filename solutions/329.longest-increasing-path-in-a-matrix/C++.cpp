class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;

        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> memo(m, vector<int>(n, 0));
        int maxLen = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                maxLen = max(maxLen, dfs(matrix, memo, i, j));
            }
        }

        return maxLen;
    }

private:
    int dfs(const vector<vector<int>>& matrix, vector<vector<int>>& memo, int i, int j) {
        if (memo[i][j] != 0) return memo[i][j];
        
        static vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int maxLen = 1;

        for (const auto& dir : directions) {
            int x = i + dir.first, y = j + dir.second;
            if (x >= 0 && x < matrix.size() && y >= 0 && y < matrix[0].size() && matrix[x][y] > matrix[i][j]) {
                maxLen = max(maxLen, 1 + dfs(matrix, memo, x, y));
            }
        }

        memo[i][j] = maxLen;
        return maxLen;
    }
};