class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3*limit: return 0
        if n <= limit: return (n+2)*(n+1)//2
        if n >= 3*limit / 2: n = 3*limit - n
        if n <= limit: return (n+2)*(n+1)//2
        else: return (n+2)*(n+1)//2 - 3*(n-limit)*(n-limit+1)//2