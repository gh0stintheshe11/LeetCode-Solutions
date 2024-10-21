class Solution {
public:
    bool isPowerOfThree(int n) {
        // The maximum power of three value that fits in a signed 32-bit integer is 1162261467 (i.e., 3^19)
        // If n is a power of three, then this number should be divisible by n with no remainder.
        return n > 0 && 1162261467 % n == 0;
    }
};