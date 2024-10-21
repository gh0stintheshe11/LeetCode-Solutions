#include <limits.h>

int divide(int dividend, int divisor) {
    // Handle edge cases
    if (divisor == 0) return INT_MAX; // Division by zero is undefined
    if (dividend == INT_MIN && divisor == -1) return INT_MAX; // Overflow case

    // Determine the sign of the result
    int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;

    // Convert both dividend and divisor to positive
    long long abs_dividend = labs(dividend);
    long long abs_divisor = labs(divisor);

    // Initialize the quotient
    long long quotient = 0;

    // Perform the division using bit manipulation
    while (abs_dividend >= abs_divisor) {
        long long temp = abs_divisor, multiple = 1;
        while (abs_dividend >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }
        abs_dividend -= temp;
        quotient += multiple;
    }

    // Apply the sign to the quotient
    quotient = sign * quotient;

    // Ensure the result is within the 32-bit signed integer range
    if (quotient > INT_MAX) return INT_MAX;
    if (quotient < INT_MIN) return INT_MIN;

    return (int)quotient;
}
