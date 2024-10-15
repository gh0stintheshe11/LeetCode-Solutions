class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        from math import gcd

        def reduce_to_one(x):
            while x % 2 == 0:
                x //= 2
            return x

        # Reduce both targetX and targetY by factor of 2 since multiplying by 2 to reach a point means x or y can be halved if even
        targetX = reduce_to_one(targetX)
        targetY = reduce_to_one(targetY)

        # Check if gcd of reduced targetX and targetY is 1
        return gcd(targetX, targetY) == 1