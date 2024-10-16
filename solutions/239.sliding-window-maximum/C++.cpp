#include <vector>
#include <deque>

class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        std::deque<int> deq;
        std::vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            // Remove the elements which are out of this window
            if (!deq.empty() && deq.front() == i - k) {
                deq.pop_front();
            }
            
            // Remove all elements smaller than the currently
            // being added element (remove useless elements)
            while (!deq.empty() && nums[deq.back()] < nums[i]) {
                deq.pop_back();
            }
            
            // Add current element at the back of the deque
            deq.push_back(i);
            
            // The element at the front of the deque is the largest element of
            // the previous window, so append it to the result as soon as
            // i becomes larger than or equal to k - 1
            if (i >= k - 1) {
                result.push_back(nums[deq.front()]);
            }
        }
        
        return result;
    }
};