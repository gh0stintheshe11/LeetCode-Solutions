#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> reconstructQueue(std::vector<std::vector<int>>& people) {
        std::sort(people.begin(), people.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            // Sort by descending height and ascending number of people in front
            return a[0] > b[0] || (a[0] == b[0] && a[1] < b[1]);
        });
        
        std::vector<std::vector<int>> queue;
        for (const auto& person : people) {
            // Insert each person at their k-th position
            queue.insert(queue.begin() + person[1], person);
        }
        
        return queue;
    }
};