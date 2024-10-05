class Solution:
    def newInteger(self, n: int) -> int:
        result = ""
        while n > 0:
            result = str(n % 9) + result
            n //= 9
        return int(result)