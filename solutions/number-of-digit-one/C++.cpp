class Solution {
public:
    int countDigitOne(int n) {
        long count = 0;
        long factor = 1;
        while (factor <= n) {
            long lowerNumbers = n - (n / factor) * factor;
            long currentDigit = (n / factor) % 10;
            long higherNumbers = n / (factor * 10);

            if (currentDigit == 0) {
                count += higherNumbers * factor;
            } else if (currentDigit == 1) {
                count += higherNumbers * factor + lowerNumbers + 1;
            } else {
                count += (higherNumbers + 1) * factor;
            }

            factor *= 10;
        }
        return count;
    }
};