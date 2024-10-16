class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLen = 0;
        int left = 0, right = 0;
        
        // Left to Right scan
        for (char c : s) {
            if (c == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLen = max(maxLen, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }

        left = right = 0;

        // Right to Left scan
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLen = max(maxLen, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }

        return maxLen;
    }
};