class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = list(map(int, str(n)))
        k = len(digits)
        return n == sum(digit ** k for digit in digits)