class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        base7 = []
        
        while num > 0:
            base7.append(str(num % 7))
            num //= 7
        
        if negative:
            base7.append('-')
        
        return ''.join(base7[::-1])