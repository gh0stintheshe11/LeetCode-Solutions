class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        if (x + y < target) return false;
        if (x == target || y == target || x + y == target) return true;
        return target % std::gcd(x, y) == 0;
    }
};