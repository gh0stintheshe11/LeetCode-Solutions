class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<bool>> isPalindrome(n, vector<bool>(n, false));
        vector<int> dp(n, 0);

        for (int i = 0; i < n; ++i) {
            int minCuts = i; // Maximum cuts equals i (cut each character)
            for (int j = 0; j <= i; ++j) {
                if (s[i] == s[j] && (i - j <= 2 || isPalindrome[j + 1][i - 1])) {
                    isPalindrome[j][i] = true;
                    minCuts = (j == 0) ? 0 : min(minCuts, dp[j - 1] + 1);
                }
            }
            dp[i] = minCuts;
        }

        return dp[n - 1];
    }
};