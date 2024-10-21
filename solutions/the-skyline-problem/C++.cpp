#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        // Create an event list
        vector<pair<int, int>> events;
        for (const auto& b : buildings) {
            events.emplace_back(b[0], -b[2]);  // Start of a building
            events.emplace_back(b[1], b[2]);   // End of a building
        }
        // Sort events first by x coordinate, then by height (starts first, ends later)
        sort(events.begin(), events.end());

        // Multiset to keep track of current heights in sorted order (a max-heap)
        multiset<int> heights = {0};
        vector<vector<int>> result;
        int prev_max_height = 0;

        for (const auto& event : events) {
            int x = event.first, h = event.second;
            if (h < 0) {  // Starting point of a building
                heights.insert(-h);
            } else {      // Ending point of a building
                heights.erase(heights.find(h));
            }

            // Check current maximum height
            int curr_max_height = *heights.rbegin();
            if (curr_max_height != prev_max_height) {
                result.push_back({x, curr_max_height});
                prev_max_height = curr_max_height;
            }
        }

        return result;
    }
};