class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int max_water = 0;
        
        while (left < right) {
            int width = right - left;
            int current_height = min(height[left], height[right]);
            max_water = max(max_water, width * current_height);
            
            if (height[left] < height[right]) {
                ++left;
            } else {
                --right;
            }
        }
        
        return max_water;
    }
};