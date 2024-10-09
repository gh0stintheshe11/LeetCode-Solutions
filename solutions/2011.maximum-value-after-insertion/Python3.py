class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)
        if n[0] == '-':
            # n is negative, insert x to minimize the value
            for i in range(1, len(n)):
                if x < n[i]:
                    return n[:i] + x + n[i:]
            return n + x
        else:
            # n is positive, insert x to maximize the value
            for i in range(len(n)):
                if x > n[i]:
                    return n[:i] + x + n[i:]
            return n + x