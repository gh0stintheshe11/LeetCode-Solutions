class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        x, y, z = sorted([a, b, c])
        if x + y <= z:
            return x + y
        return (x + y + z) // 2