import re
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        
        numerator, denominator = 0, 1
        
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            numerator = numerator * denom + num * denominator
            denominator *= denom
            gcd = math.gcd(numerator, denominator)
            numerator //= gcd
            denominator //= gcd
        
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        
        return f"{numerator}/{denominator}"