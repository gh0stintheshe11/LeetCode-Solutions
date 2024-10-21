class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), cnt = 0;
        vector<pair<int, int> > D = {{-1,0},{1,0},{0,-1},{0,1}};
        vector<vector<int> > match(m, vector<int> (n, -1));
        vector<vector<int> > vis(m, vector<int> (n, -1));

        function<int(int,int,int)> dfs = [&](int i, int j, int v) {
            for (const auto &[di, dj] : D) {
                int x = i+di, y = j+dj;
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] && vis[x][y] != v) {
                    vis[x][y] = v;
					// found an augment path
                    if (match[x][y] == -1 || dfs(match[x][y]/n, match[x][y]%n, v)) {
                        match[x][y] = i*n+j;
                        match[i][j] = x*n+y;
                        return 1;
                    }
                }
            }
            return 0;
        };

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) if (grid[i][j] && match[i][j] == -1)
                cnt += dfs(i, j, vis[i][j] = i*n+j);
        return cnt;
    }
};