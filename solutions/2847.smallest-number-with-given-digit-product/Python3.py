class Solution:
    def smallestNumber(self, n: int) -> str:
        if n == 1:
            return "1"
        
        digits = []
        
        def factorize(n):
            for i in range(9, 1, -1):
                while n % i == 0:
                    n //= i
                    digits.append(i)
            return n
        
        if factorize(n) > 1:
            return "-1"
        
        digits.sort()
        return "".join(map(str, digits))