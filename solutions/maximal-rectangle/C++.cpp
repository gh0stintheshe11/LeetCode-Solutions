class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int maxArea = 0;
        int n = matrix.size();
        int m = matrix[0].size();
        vector<int> height(m, 0), left(m, 0), right(m, m);
        
        for (int i = 0; i < n; ++i) {
            int curLeft = 0, curRight = m;
            // update height
            for (int j = 0; j < m; ++j) {
                if (matrix[i][j] == '1') height[j]++;
                else height[j] = 0;
            }
            // update left
            for (int j = 0; j < m; ++j) {
                if (matrix[i][j] == '1') left[j] = max(left[j], curLeft);
                else {
                    left[j] = 0;
                    curLeft = j + 1;
                }
            }
            // update right
            for (int j = m - 1; j >= 0; --j) {
                if (matrix[i][j] == '1') right[j] = min(right[j], curRight);
                else {
                    right[j] = m;
                    curRight = j;
                }
            }
            // update area
            for (int j = 0; j < m; ++j) {
                maxArea = max(maxArea, (right[j] - left[j]) * height[j]);
            }
        }
        return maxArea;
    }
};