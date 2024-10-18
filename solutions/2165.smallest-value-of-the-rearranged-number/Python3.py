class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        num_str = str(abs(num))
        digits = sorted(num_str)
        
        if num > 0:
            # Find the first non-zero digit and place it at the start
            for i, digit in enumerate(digits):
                if digit != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int(''.join(digits))
        else:
            # For negative numbers, sort the digits in descending order
            digits.sort(reverse=True)
            return -int(''.join(digits))