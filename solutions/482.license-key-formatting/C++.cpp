class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        string stripped;
        // Strip all dashes and convert to uppercase
        for (char c : s) {
            if (c != '-') {
                stripped += toupper(c);
            }
        }

        int n = stripped.size();
        string result;
        int firstGroupLength = n % k;
        if (firstGroupLength > 0) {
            result = stripped.substr(0, firstGroupLength);
        }

        for (int i = firstGroupLength; i < n; i += k) {
            if (!result.empty()) result += '-';
            result += stripped.substr(i, k);
        }

        return result;
    }
};