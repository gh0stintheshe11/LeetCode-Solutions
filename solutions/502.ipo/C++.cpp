#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int findMaximizedCapital(int k, int w, std::vector<int>& profits, std::vector<int>& capital) {
        std::vector<std::pair<int, int>> projects;
        for (int i = 0; i < profits.size(); ++i) {
            projects.emplace_back(capital[i], profits[i]);
        }
        
        std::sort(projects.begin(), projects.end());
        
        std::priority_queue<int> maxHeap;
        int i = 0;
        while (k--) {
            while (i < projects.size() && projects[i].first <= w) {
                maxHeap.push(projects[i].second);
                ++i;
            }
            
            if (!maxHeap.empty()) {
                w += maxHeap.top();
                maxHeap.pop();
            } else {
                break;
            }
        }
        
        return w;
    }
};