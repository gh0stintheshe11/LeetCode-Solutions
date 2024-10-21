class Solution:
    def findNumber(self) -> int:
        ans = 0
        baseline = commonBits(0)
        for i in range(30):
            b = 1 << i
            res = commonBits(b)
            if res > baseline:
                ans |= b
            baseline = res
        return ans