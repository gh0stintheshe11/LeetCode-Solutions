class Solution {
public:
    int hammingDistance(int x, int y) {
        int xorValue = x ^ y;
        int distance = 0;
        while (xorValue) {
            distance += xorValue & 1;
            xorValue >>= 1;
        }
        return distance;
    }
};