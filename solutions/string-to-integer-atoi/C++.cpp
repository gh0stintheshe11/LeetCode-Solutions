#include <climits>
#include <cctype>
#include <string>

class Solution {
public:
    int myAtoi(std::string s) {
        int i = 0, n = s.length();
        // Skip leading spaces
        while (i < n && isspace(s[i])) {
            i++;
        }
        
        // Handle optional sign
        int sign = 1;
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
        
        // Convert numbers
        long long result = 0;
        while (i < n && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');
            i++;
            
            // Check for overflow
            if (result * sign <= INT_MIN) {
                return INT_MIN;
            }
            if (result * sign >= INT_MAX) {
                return INT_MAX;
            }
        }
        
        return result * sign;
    }
};