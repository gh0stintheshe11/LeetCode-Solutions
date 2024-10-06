#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        int m = targetGrid.size();
        int n = targetGrid[0].size();
        vector<int> top(61, m), bottom(61, -1), left(61, n), right(61, -1);
        unordered_set<int> colors;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int c = targetGrid[i][j];
                colors.insert(c);
                top[c] = min(top[c], i);
                bottom[c] = max(bottom[c], i);
                left[c] = min(left[c], j);
                right[c] = max(right[c], j);
            }
        }

        vector<unordered_set<int>> dependencies(61);
        vector<int> indegree(61, 0);

        for (int c : colors) {
            for (int i = top[c]; i <= bottom[c]; ++i) {
                for (int j = left[c]; j <= right[c]; ++j) {
                    if (targetGrid[i][j] != c) {
                        if (dependencies[c].insert(targetGrid[i][j]).second) {
                            indegree[targetGrid[i][j]]++;
                        }
                    }
                }
            }
        }

        queue<int> q;
        for (int c : colors) {
            if (indegree[c] == 0) {
                q.push(c);
            }
        }

        int printed = 0;
        while (!q.empty()) {
            int c = q.front();
            q.pop();
            printed++;

            for (int dep : dependencies[c]) {
                if (--indegree[dep] == 0) {
                    q.push(dep);
                }
            }
        }

        return printed == colors.size();
    }
};