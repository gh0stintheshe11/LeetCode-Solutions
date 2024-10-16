class Solution {
public:
    bool isNumber(string s) {
        int n = s.length();
        int i = 0;

        // Skip leading whitespace
        while (i < n && s[i] == ' ') i++;

        // Handle optional sign
        if (i < n && (s[i] == '+' || s[i] == '-')) i++;

        bool isNumeric = false;
        // Process digits before the decimal point
        while (i < n && isdigit(s[i])) {
            i++;
            isNumeric = true;
        }

        // Process the decimal point and digits after it
        if (i < n && s[i] == '.') {
            i++;
            while (i < n && isdigit(s[i])) {
                i++;
                isNumeric = true;
            }
        }

        // Process the exponent part
        if (isNumeric && i < n && (s[i] == 'e' || s[i] == 'E')) {
            i++;
            isNumeric = false;
            if (i < n && (s[i] == '+' || s[i] == '-')) i++;
            while (i < n && isdigit(s[i])) {
                i++;
                isNumeric = true;
            }
        }

        // Skip trailing whitespace
        while (i < n && s[i] == ' ') i++;

        return isNumeric && i == n;
    }
};