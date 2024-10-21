class Solution {
public:
    int findSubstringInWraproundString(string s) {
        vector<int> dp(26, 0); // To store the max length ending with each character
        int n = s.length();
        int maxLen = 0; // Current max length of valid substring in wraparound

        for (int i = 0; i < n; ++i) {
            if (i > 0 && (s[i] == s[i-1] + 1 || (s[i-1] == 'z' && s[i] == 'a'))) {
                maxLen++;
            } else {
                maxLen = 1;
            }
            int index = s[i] - 'a';
            dp[index] = max(dp[index], maxLen);
        }

        int result = 0;
        for (int count : dp) {
            result += count;
        }
        return result;
    }
};