class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;
        int n = heights.size();
        stack<int> s;
        
        for (int i = 0; i <= n; i++) {
            while (!s.empty() && (i == n || heights[s.top()] >= heights[i])) {
                int height = heights[s.top()];
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                maxArea = max(maxArea, height * width);
            }
            s.push(i);
        }
        
        return maxArea;
    }
};