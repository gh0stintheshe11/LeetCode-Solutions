#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) return 0;
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int arrows = 1;
        int lastEnd = points[0][1];
        for (const auto& point : points) {
            if (point[0] > lastEnd) {
                arrows++;
                lastEnd = point[1];
            }
        }
        return arrows;
    }
};