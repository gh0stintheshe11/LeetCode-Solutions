class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.length(), m = s2.length(), l = s3.length();
        if (n + m != l) return false;

        vector<bool> dp(m + 1, false);
        dp[0] = true;

        for (int j = 1; j <= m; ++j) {
            dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
        }

        for (int i = 1; i <= n; ++i) {
            dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
            for (int j = 1; j <= m; ++j) {
                dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1]) || (dp[j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }

        return dp[m];
    }
};