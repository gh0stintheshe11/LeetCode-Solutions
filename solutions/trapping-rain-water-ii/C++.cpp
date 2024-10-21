#include <vector>
#include <queue>
#include <utility>
using namespace std;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.empty() || heightMap[0].empty()) return 0;

        int m = heightMap.size(), n = heightMap[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        auto cmp = [](const pair<int, pair<int, int>>& a, const pair<int, pair<int, int>>& b) {
            return a.first > b.first;
        };
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, decltype(cmp)> pq(cmp);

        for (int i = 0; i < m; ++i) {
            pq.push({heightMap[i][0], {i, 0}});
            pq.push({heightMap[i][n - 1], {i, n - 1}});
            visited[i][0] = visited[i][n - 1] = true;
        }
        for (int j = 1; j < n - 1; ++j) {
            pq.push({heightMap[0][j], {0, j}});
            pq.push({heightMap[m - 1][j], {m - 1, j}});
            visited[0][j] = visited[m - 1][j] = true;
        }

        int waterTrapped = 0;
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!pq.empty()) {
            auto cell = pq.top(); pq.pop();
            int height = cell.first;
            int x = cell.second.first;
            int y = cell.second.second;

            for (const auto& dir : directions) {
                int nx = x + dir[0];
                int ny = y + dir[1];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    waterTrapped += max(0, height - heightMap[nx][ny]);
                    pq.push({max(height, heightMap[nx][ny]), {nx, ny}});
                }
            }
        }

        return waterTrapped;
    }
};