class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from math import gcd
        
        lcm = (p * q) // gcd(p, q)
        reflect_p = lcm // p
        reflect_q = lcm // q
        
        if reflect_p % 2 == 0:
            return 0
        if reflect_q % 2 == 0:
            return 2
        return 1