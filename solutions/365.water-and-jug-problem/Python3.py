import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if target % math.gcd(x, y) == 0:
            return True
        return False