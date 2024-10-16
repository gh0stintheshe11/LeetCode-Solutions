class Solution {
public:
    const int MOD = 1337;
    
    int powmod(int x, int y, int mod) {
        int res = 1;
        x = x % mod;
        while (y > 0) {
            if (y % 2 == 1) {
                res = (res * x) % mod;
            }
            y = y >> 1;
            x = (x * x) % mod;
        }
        return res;
    }
    
    int superPow(int a, vector<int>& b) {
        if (b.empty()) return 1;
        int lastDigit = b.back();
        b.pop_back();

        int part1 = powmod(superPow(a, b), 10, MOD);
        int part2 = powmod(a, lastDigit, MOD);

        return (part1 * part2) % MOD;
    }
};