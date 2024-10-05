class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        res = 10
        unique_digits = 9
        available_numbers = 9
        
        while n > 1 and available_numbers > 0:
            unique_digits *= available_numbers
            res += unique_digits
            available_numbers -= 1
            n -= 1
            
        return res