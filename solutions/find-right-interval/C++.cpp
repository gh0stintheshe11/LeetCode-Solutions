#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<pair<int, int>> startIndices(n);

        for (int i = 0; i < n; ++i) {
            startIndices[i] = {intervals[i][0], i};
        }

        sort(startIndices.begin(), startIndices.end());

        vector<int> result(n);

        for (int i = 0; i < n; ++i) {
            int target = intervals[i][1];
            int left = 0, right = n - 1;
            int index = -1;

            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (startIndices[mid].first >= target) {
                    index = startIndices[mid].second;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            result[i] = index;
        }

        return result;
    }
};