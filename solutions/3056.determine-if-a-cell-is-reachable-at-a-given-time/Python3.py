class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        chebyshev_distance = max(abs(fx - sx), abs(fy - sy))
        
        if sx == fx and sy == fy:
            return t != 1
        
        return chebyshev_distance <= t