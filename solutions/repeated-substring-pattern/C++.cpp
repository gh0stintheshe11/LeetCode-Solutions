class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for (int len = 1; len <= n / 2; ++len) {
            if (n % len == 0) {
                string substr = s.substr(0, len);
                string pattern = "";
                for (int k = 0; k < n / len; ++k) {
                    pattern += substr;
                }
                if (pattern == s) {
                    return true;
                }
            }
        }
        return false;
    }
};