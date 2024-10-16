class Solution {
public:
    string kthSmallestPath(vector<int>& destination, int k) {
        int row = destination[0];
        int column = destination[1];
        string result = "";
        int total_steps = row + column;
        
        // Lambda to calculate nCr (combinatorial number)
        auto nCr = [](int n, int r) {
            if (r > n) return 0;
            if (r > n - r) r = n - r;
            long long result = 1;
            for (int i = 0; i < r; ++i) {
                result *= (n - i);
                result /= (i + 1);
            }
            return (int)result;
        };
        
        for (int i = 0; i < total_steps; ++i) {
            if (column == 0) {
                result += 'V';
                continue;
            }
            if (row == 0) {
                result += 'H';
                continue;
            }
            
            // If we choose 'H', then we need nCr(row+column-1, row) ways
            int chooseH = nCr(row + column - 1, column - 1);
            if (k <= chooseH) {
                result += 'H';
                column--;
            } else {
                result += 'V';
                row--;
                k -= chooseH;
            }
        }
        return result;
    }
};