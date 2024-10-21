class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        
        string s = "1";
        for (int i = 2; i <= n; ++i) {
            string next = "";
            int count = 1;
            for (int j = 1; j <= s.size(); ++j) {
                if (j < s.size() && s[j] == s[j - 1]) {
                    ++count;
                } else {
                    next += to_string(count) + s[j - 1];
                    count = 1;
                }
            }
            s = next;
        }
        
        return s;
    }
};