class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        odd_digits = sorted([d for d in digits if int(d) % 2 == 1], reverse=True)
        even_digits = sorted([d for d in digits if int(d) % 2 == 0], reverse=True)
        
        for i in range(len(digits)):
            if int(digits[i]) % 2 == 0:
                digits[i] = even_digits.pop(0)
            else:
                digits[i] = odd_digits.pop(0)
        
        return int("".join(digits))