#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return 0;

        // dp[i] will store a map of differences to their counts ending at index i
        vector<unordered_map<long long, int>> dp(n);
        int total = 0;

        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                // Avoid overflow in calculating difference
                long long diff = (long long)nums[i] - (long long)nums[j];

                // Retrieve the current number of arithmetic slices ending at `j` with difference `diff`
                int count = dp[j][diff];

                // Increase the total by the number of arithmetic slices ending with `nums[i]`
                total += count;

                // Extend the sequences ending at `j` with difference `diff` to include `nums[i]`
                dp[i][diff] += count + 1;
            }
        }

        return total;
    }
};