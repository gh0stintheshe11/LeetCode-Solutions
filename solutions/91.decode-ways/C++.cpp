class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        if (n == 0 || s[0] == '0') return 0;
        
        int prev2 = 1, prev1 = 1; // prev2 is dp[i-2], prev1 is dp[i-1]
        
        for (int i = 1; i < n; ++i) {
            int current = 0;
            
            if (s[i] != '0') {
                current = prev1;
            }
            
            int twoDigit = (s[i-1] - '0') * 10 + (s[i] - '0');
            if (twoDigit >= 10 && twoDigit <= 26) {
                current += prev2;
            }
            
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
};