#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> left, right;
        vector<double> medians;
        
        for (int i = 0; i < nums.size(); ++i) {
            // Insert into the appropriate heap
            if (!left.empty() && nums[i] <= *left.rbegin()) {
                left.insert(nums[i]);
            } else {
                right.insert(nums[i]);
            }
            
            // Remove element that's sliding out
            if (i >= k) {
                if (left.find(nums[i - k]) != left.end()) {
                    left.erase(left.find(nums[i - k]));
                } else {
                    right.erase(right.find(nums[i - k]));
                }
            }
            
            // Balance the heaps
            if (left.size() > right.size() + 1) {
                right.insert(*left.rbegin());
                left.erase(--left.end());
            } else if (right.size() > left.size()) {
                left.insert(*right.begin());
                right.erase(right.begin());
            }
            
            // Record the median
            if (i >= k - 1) {
                if (k % 2 == 0) {
                    medians.push_back(((double)(*left.rbegin()) + *right.begin()) / 2);
                } else {
                    medians.push_back(*left.rbegin());
                }
            }
        }
        
        return medians;
    }
};