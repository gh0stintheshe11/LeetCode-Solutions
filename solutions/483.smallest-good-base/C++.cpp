class Solution {
public:
    string smallestGoodBase(string n) {
        unsigned long long N = stoull(n);
        
        for (int m = 60; m >= 2; --m) {
            unsigned long long k = pow(N, 1.0 / m);
            if (k > 1) {
                unsigned long long sum = 1, base = 1;
                for (int i = 0; i < m; ++i) {
                    base *= k;
                    sum += base;
                }
                if (sum == N) {
                    return to_string(k);
                }
            }
        }

        return to_string(N - 1); // When m=1, the smallest good base is N-1.
    }
};