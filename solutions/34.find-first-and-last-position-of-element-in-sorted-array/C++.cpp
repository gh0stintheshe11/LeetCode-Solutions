#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return {lowerBound(nums, target), upperBound(nums, target)};
    }
    
    int lowerBound(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1, ans = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                if (nums[mid] == target) ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
    
    int upperBound(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1, ans = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else {
                if (nums[mid] == target) ans = mid;
                left = mid + 1;
            }
        }
        return ans;
    }
};