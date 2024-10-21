class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        total = 0
        for digit in str(n):
            total += sign * int(digit)
            sign *= -1
        return total