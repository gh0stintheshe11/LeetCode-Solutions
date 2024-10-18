class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        
        memo = {}
        
        def P(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            memo[(a, b)] = 0.25 * (P(a - 100, b) + P(a - 75, b - 25) + P(a - 50, b - 50) + P(a - 25, b - 75))
            return memo[(a, b)]
        
        return P(n, n)