class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum_is_even(n):
            return sum(int(digit) for digit in str(n)) % 2 == 0
        
        count = 0
        for i in range(1, num + 1):
            if digit_sum_is_even(i):
                count += 1
        return count