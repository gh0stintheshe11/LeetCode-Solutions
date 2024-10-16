class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        int left = 1, right = x, result = 0;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mid <= x / mid) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }
};