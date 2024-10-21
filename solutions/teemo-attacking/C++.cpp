class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if (timeSeries.empty()) return 0;

        int totalDuration = 0;
        for (int i = 0; i < timeSeries.size() - 1; ++i) {
            totalDuration += min(duration, timeSeries[i+1] - timeSeries[i]);
        }
        return totalDuration + duration;
    }
};