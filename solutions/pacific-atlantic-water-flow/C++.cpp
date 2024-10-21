class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};
        
        int m = heights.size();
        int n = heights[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0, INT_MIN);
            dfs(heights, atlantic, i, n - 1, INT_MIN);
        }
        
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j, INT_MIN);
            dfs(heights, atlantic, m - 1, j, INT_MIN);
        }
        
        vector<vector<int>> result;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
    
private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int x, int y, int prevHeight) {
        int m = heights.size();
        int n = heights[0].size();
        if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y] || heights[x][y] < prevHeight) 
            return;
        
        visited[x][y] = true;
        dfs(heights, visited, x + 1, y, heights[x][y]);
        dfs(heights, visited, x - 1, y, heights[x][y]);
        dfs(heights, visited, x, y + 1, heights[x][y]);
        dfs(heights, visited, x, y - 1, heights[x][y]);
    }
};