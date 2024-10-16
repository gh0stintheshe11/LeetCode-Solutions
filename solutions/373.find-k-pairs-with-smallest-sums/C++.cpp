#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<vector<int>> result;
        if (nums1.empty() || nums2.empty() || k <= 0) return result;

        auto comp = [&](const pair<int, int>& a, const pair<int, int>& b) {
            return nums1[a.first] + nums2[a.second] > nums1[b.first] + nums2[b.second];
        };
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> minHeap(comp);
        
        for (int i = 0; i < nums1.size() && i < k; ++i) {
            minHeap.emplace(i, 0);
        }
        
        while (!minHeap.empty() && result.size() < k) {
            auto [i, j] = minHeap.top();
            minHeap.pop();
            result.push_back({nums1[i], nums2[j]});
            if (j + 1 < nums2.size()) {
                minHeap.emplace(i, j + 1);
            }
        }
        
        return result;
    }
};