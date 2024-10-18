class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        num1, num2 = [], []

        for i in range(len(digits)):
            if i % 2 == 0:
                num1.append(digits[i])
            else:
                num2.append(digits[i])

        return int("".join(num1)) + int("".join(num2))