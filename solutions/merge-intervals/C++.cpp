class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        // Sort intervals based on their start times
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        for (const auto& interval : intervals) {
            // If merged is empty or current interval does not overlap with the last merged interval
            // simply add the interval to the merged list
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                // Overlapping intervals, merge them by updating the end of the last interval
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        
        return merged;
    }
};