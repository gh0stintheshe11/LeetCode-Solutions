class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum_digits = 0
        while n > 0:
            sum_digits += n % k
            n //= k
        return sum_digits