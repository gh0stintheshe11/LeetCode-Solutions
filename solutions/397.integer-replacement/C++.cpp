class Solution {
public:
    int integerReplacement(int n) {
        if (n == 1) return 0;
        if (n % 2 == 0) {
            return 1 + integerReplacement(n / 2);
        } else {
            if (n == INT_MAX) return 32; // special handling for overflow case
            return 1 + min(integerReplacement(n + 1), integerReplacement(n - 1));
        }
    }
};