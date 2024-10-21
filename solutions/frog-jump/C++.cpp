#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    bool canCross(std::vector<int>& stones) {
        std::unordered_map<int, std::unordered_set<int>> stoneJumps;
        stoneJumps[stones[0]].insert(1);

        for (int i = 0; i < stones.size(); ++i) {
            int position = stones[i];
            if (stoneJumps.find(position) != stoneJumps.end()) {
                for (int k : stoneJumps[position]) {
                    int reach = position + k;
                    if (reach == stones.back()) {
                        return true;
                    }
                    if (std::binary_search(stones.begin(), stones.end(), reach)) {
                        if (k - 1 > 0) stoneJumps[reach].insert(k - 1);
                        stoneJumps[reach].insert(k);
                        stoneJumps[reach].insert(k + 1);
                    }
                }
            }
        }
        
        return false;
    }
};