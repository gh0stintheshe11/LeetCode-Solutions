class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        if (mat.empty() || mat[0].empty()) return {};
        
        int m = mat.size(), n = mat[0].size();
        vector<int> result;
        result.reserve(m * n);
        
        for (int d = 0; d < m + n - 1; ++d) {
            int r = d < n ? 0 : d - n + 1;
            int c = d < n ? d : n - 1;
            
            vector<int> diagonal;
            while (r < m && c >= 0) {
                diagonal.push_back(mat[r][c]);
                ++r;
                --c;
            }
            
            if (d % 2 == 0) {
                std::reverse(diagonal.begin(), diagonal.end());
            }
            
            result.insert(result.end(), diagonal.begin(), diagonal.end());
        }
        
        return result;
    }
};