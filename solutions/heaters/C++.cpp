#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        
        int maxRadius = 0;
        for (int house : houses) {
            int heaterIndex = lower_bound(heaters.begin(), heaters.end(), house) - heaters.begin();
            int dist1 = (heaterIndex < heaters.size()) ? abs(heaters[heaterIndex] - house) : INT_MAX;
            int dist2 = (heaterIndex > 0) ? abs(heaters[heaterIndex - 1] - house) : INT_MAX;
            int minDist = min(dist1, dist2);
            maxRadius = max(maxRadius, minDist);
        }
        
        return maxRadius;
    }
};