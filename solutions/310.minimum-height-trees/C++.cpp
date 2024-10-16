#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0};
        vector<unordered_set<int>> adj(n);
        for (auto& edge : edges) {
            adj[edge[0]].insert(edge[1]);
            adj[edge[1]].insert(edge[0]);
        }
        
        vector<int> leaves;
        for (int i = 0; i < n; i++) {
            if (adj[i].size() == 1) {
                leaves.push_back(i);
            }
        }
        
        while (n > 2) {
            n -= leaves.size();
            vector<int> new_leaves;
            for (int leaf : leaves) {
                int neighbor = *adj[leaf].begin();
                adj[neighbor].erase(leaf);
                if (adj[neighbor].size() == 1) {
                    new_leaves.push_back(neighbor);
                }
            }
            leaves = new_leaves;
        }
        
        return leaves;
    }
};