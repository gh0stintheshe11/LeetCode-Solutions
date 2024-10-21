class Solution {
public:
    int strongPasswordChecker(string password) {
        int n = password.size();
        bool hasLower = false, hasUpper = false, hasDigit = false;
        for (char c : password) {
            if (islower(c)) hasLower = true;
            else if (isupper(c)) hasUpper = true;
            else if (isdigit(c)) hasDigit = true;
        }
        
        int missingTypes = !hasLower + !hasUpper + !hasDigit;
        
        int replace = 0, oneDeletions = 0, twoDeletions = 0;
        for (int i = 2; i < n; ) {
            if (password[i] == password[i-1] && password[i-1] == password[i-2]) {
                int length = 2;
                while (i < n && password[i] == password[i-1]) {
                    ++length;
                    ++i;
                }
                replace += length / 3;
                if (length % 3 == 0) oneDeletions++;
                else if (length % 3 == 1) twoDeletions++;
            } else {
                ++i;
            }
        }
        
        if (n < 6) {
            return max(missingTypes, 6 - n);
        } else if (n <= 20) {
            return max(missingTypes, replace);
        } else {
            int deleteOperations = n - 20;
            replace -= min(deleteOperations, oneDeletions * 1) / 1;
            replace -= min(max(deleteOperations - oneDeletions, 0), twoDeletions * 2) / 2;
            replace -= max(deleteOperations - oneDeletions - 2 * twoDeletions, 0) / 3;
            return deleteOperations + max(missingTypes, replace);
        }
    }
};