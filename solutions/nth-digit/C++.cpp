class Solution {
public:
    int findNthDigit(int n) {
        long base = 9, digits = 1;
        // Calculate how many digits there are in the number containing the nth digit
        while (n > base * digits) {
            n -= base * digits;
            base *= 10;
            digits++;
        }

        // Calculate the actual number containing the nth digit
        long index = n - 1;
        long start = pow(10, digits - 1);
        long number = start + index / digits;

        // Identify the exact digit within the number
        string s = to_string(number);
        return s[index % digits] - '0';
    }
};