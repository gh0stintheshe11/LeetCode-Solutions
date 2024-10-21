#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <climits>

class Solution {
public:
    int findRotateSteps(std::string ring, std::string key) {
        int m = ring.size();
        int n = key.size();
        
        // Mapping from character to all indices it appears in the ring
        std::unordered_map<char, std::vector<int>> charToIndex;
        for (int i = 0; i < m; ++i) {
            charToIndex[ring[i]].push_back(i);
        }
        
        // Memorization for DP
        std::vector<std::vector<int>> dp(n, std::vector<int>(m, -1));

        // Helper function for DP
        auto dfs = [&](auto&& self, int keyIdx, int ringPos) -> int {
            if (keyIdx == n) {
                return 0;
            }
            if (dp[keyIdx][ringPos] != -1) {
                return dp[keyIdx][ringPos];
            }

            char currentKeyChar = key[keyIdx];
            int minSteps = INT_MAX;
            for (int ringIdx : charToIndex[currentKeyChar]) {
                int diff = std::abs(ringPos - ringIdx);
                int step = std::min(diff, m - diff) + 1;
                minSteps = std::min(minSteps, step + self(self, keyIdx + 1, ringIdx));
            }

            return dp[keyIdx][ringPos] = minSteps;
        };

        return dfs(dfs, 0, 0);
    }
};