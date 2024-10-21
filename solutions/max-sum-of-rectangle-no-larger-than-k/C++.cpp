#include <vector>
#include <set>
#include <climits>

using namespace std;

class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        if (matrix.empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        int maxSum = INT_MIN;

        for (int left = 0; left < n; ++left) {
            vector<int> sums(m, 0);
            for (int right = left; right < n; ++right) {
                for (int i = 0; i < m; ++i) {
                    sums[i] += matrix[i][right];
                }
                
                set<int> accuSet;
                accuSet.insert(0);
                int currSum = 0;
                for (int sum : sums) {
                    currSum += sum;
                    auto it = accuSet.lower_bound(currSum - k);
                    if (it != accuSet.end()) {
                        maxSum = max(maxSum, currSum - *it);
                    }
                    accuSet.insert(currSum);
                }
            }
        }
        return maxSum;
    }
};