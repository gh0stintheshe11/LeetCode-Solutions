class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0', '1', '8', '2', '5', '6', '9'}
        different = {'2', '5', '6', '9'}

        def isGood(x):
            s = set(str(x))
            return s.issubset(valid) and any(c in different for c in s)

        return sum(isGood(x) for x in range(1, n+1))