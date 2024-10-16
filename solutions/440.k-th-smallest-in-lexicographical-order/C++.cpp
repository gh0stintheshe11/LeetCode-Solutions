class Solution {
public:
    int findKthNumber(int n, int k) {
        auto countSteps = [&](long long curr, long long n) {
            long long steps = 0;
            long long first = curr, last = curr;
            while (first <= n) {
                steps += min(last, (long long)n) - first + 1;
                first *= 10;
                last = last * 10 + 9;
            }
            return steps;
        };

        long long curr = 1; 
        k -= 1; 
        while (k > 0) {
            int steps = countSteps(curr, n);
            if (steps <= k) {
                k -= steps;
                curr += 1;
            } else {
                curr *= 10;
                k -= 1;
            }
        }
        return curr;
    }
};