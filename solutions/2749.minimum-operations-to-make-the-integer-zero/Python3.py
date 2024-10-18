class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for ops in range(61):
            target = num1 - ops * num2
            if target < 0:
                continue
            if bin(target).count('1') <= ops and target >= ops:
                return ops
        return -1