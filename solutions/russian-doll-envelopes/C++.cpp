#include <vector>
#include <algorithm>

class Solution {
public:
    int maxEnvelopes(std::vector<std::vector<int>>& envelopes) {
        if (envelopes.empty()) return 0;
        
        std::sort(envelopes.begin(), envelopes.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] == b[0] ? b[1] < a[1] : a[0] < b[0];
        });
        
        std::vector<int> dp;
        for (const auto& env : envelopes) {
            auto it = std::lower_bound(dp.begin(), dp.end(), env[1]);
            if (it == dp.end()) {
                dp.push_back(env[1]);
            } else {
                *it = env[1];
            }
        }
        
        return dp.size();
    }
};