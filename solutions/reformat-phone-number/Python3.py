class Solution:
    def reformatNumber(self, number: str) -> str:
        # Remove all spaces and dashes from the input
        digits = ''.join(filter(str.isdigit, number))
        
        n = len(digits)
        result = []
        i = 0
        
        while n > 0:
            if n > 4:
                # Take the first 3 digits
                result.append(digits[i:i+3])
                i += 3
                n -= 3
            elif n == 4:
                # Take two groups of 2 digits
                result.append(digits[i:i+2])
                i += 2
                result.append(digits[i:i+2])
                break
            elif n == 3:
                # Take all 3 digits
                result.append(digits[i:i+3])
                break
            elif n == 2:
                # Take the last 2 digits
                result.append(digits[i:i+2])
                break
                
        return '-'.join(result)