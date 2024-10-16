class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1) return 9;
        
        int upper = pow(10, n) - 1;
        int lower = upper / 10;
        
        for (int left = upper; left > lower; --left) {
            long p = createPalindrome(left);
            for (long x = upper; x * x >= p; --x) {
                if (p % x == 0 && p / x <= upper) {
                    return p % 1337;
                }
            }
        }
        
        return -1;
    }

private:
    long createPalindrome(int left) {
        string s = to_string(left);
        reverse(s.begin(), s.end());
        return stol(to_string(left) + s);
    }
};