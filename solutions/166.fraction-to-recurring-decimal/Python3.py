class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Append the integer part
        result.append(str(numerator // denominator))
        numerator %= denominator
        
        if numerator == 0:
            return "".join(result)
        
        result.append(".")
        
        # Handle the fractional part
        remainder_map = {}
        while numerator != 0:
            if numerator in remainder_map:
                result.insert(remainder_map[numerator], "(")
                result.append(")")
                break
            
            remainder_map[numerator] = len(result)
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator
        
        return "".join(result)