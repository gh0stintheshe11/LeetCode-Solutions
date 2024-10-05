#include <stdbool.h>
#include <string.h>

bool isMatch(char* s, char* p) {
    int m = strlen(s);
    int n = strlen(p);

    // Create a DP table with dimensions (m+1) x (n+1)
    bool dp[m + 1][n + 1];

    // Initialize all values to false
    for (int i = 0; i <= m; i++)
        for (int j = 0; j <= n; j++)
            dp[i][j] = false;

    // Empty pattern matches empty string
    dp[0][0] = true;

    // Handle patterns like a*, a*b*, a*b*c* that can match an empty string
    for (int j = 2; j <= n; j += 2) {
        if (p[j - 1] == '*' && dp[0][j - 2])
            dp[0][j] = true;
    }

    // Fill the DP table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                // Zero occurrence of the preceding element
                dp[i][j] = dp[i][j - 2];

                // One or more occurrences if the preceding element matches
                if (p[j - 2] == s[i - 1] || p[j - 2] == '.') {
                    dp[i][j] |= dp[i - 1][j];
                }
            } else if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {
                // Current characters match
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Characters do not match
                dp[i][j] = false;
            }
        }
    }

    return dp[m][n];
}
