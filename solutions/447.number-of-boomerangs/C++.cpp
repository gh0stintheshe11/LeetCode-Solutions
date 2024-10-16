#include <vector>
#include <unordered_map>
#include <cmath>

class Solution {
public:
    int numberOfBoomerangs(std::vector<std::vector<int>>& points) {
        int result = 0;
        for (auto& p : points) {
            std::unordered_map<int, int> distanceCount;
            for (auto& q : points) {
                int dx = p[0] - q[0];
                int dy = p[1] - q[1];
                int dist = dx * dx + dy * dy;
                distanceCount[dist]++;
            }
            for (auto& [dist, count] : distanceCount) {
                result += count * (count - 1);
            }
        }
        return result;
    }
};