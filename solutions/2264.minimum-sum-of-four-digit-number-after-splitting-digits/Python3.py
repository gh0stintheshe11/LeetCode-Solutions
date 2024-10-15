class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        new1 = int(digits[0] + digits[2])
        new2 = int(digits[1] + digits[3])
        return new1 + new2