class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x):
            return sum(int(c) for c in str(x))
        
        if digit_sum(n) <= target:
            return 0
        
        x = 0
        digit_power = 1
        
        while digit_sum(n) > target:
            current_digit = (n // digit_power) % 10
            addition = (10 - current_digit) % 10 * digit_power
            x += addition
            n += addition
            digit_power *= 10
        
        return x