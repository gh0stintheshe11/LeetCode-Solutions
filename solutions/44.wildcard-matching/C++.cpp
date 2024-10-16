class Solution {
public:
    bool isMatch(string s, string p) {
        int sLen = s.length(), pLen = p.length();
        vector<vector<bool>> dp(sLen + 1, vector<bool>(pLen + 1, false));
        
        dp[0][0] = true;
        
        for (int j = 1; j <= pLen; ++j) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        for (int i = 1; i <= sLen; ++i) {
            for (int j = 1; j <= pLen; ++j) {
                if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        
        return dp[sLen][pLen];
    }
};