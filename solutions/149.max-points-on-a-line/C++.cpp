#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        if (points.size() <= 2) return points.size();
        int max_points = 0;
        for (int i = 0; i < points.size(); ++i) {
            unordered_map<double, int> slope_count; 
            int duplicate = 1;
            for (int j = i + 1; j < points.size(); ++j) {
                if (points[i][0] == points[j][0] && points[i][1] == points[j][1]) {
                    ++duplicate; 
                } else {
                    double slope = numeric_limits<double>::infinity();
                    if (points[i][0] != points[j][0]) { 
                        slope = 1.0 * (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]);
                    }
                    ++slope_count[slope];
                }
            }
            int current_max = duplicate;
            for (auto& pair : slope_count) {
                current_max = max(current_max, pair.second + duplicate);
            }
            max_points = max(max_points, current_max);
        }
        return max_points;
    }
};