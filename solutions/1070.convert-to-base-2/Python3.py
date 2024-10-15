class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = []
        while n != 0:
            n, remainder = divmod(n, -2)
            if remainder < 0:
                remainder += 2
                n += 1
            res.append(str(remainder))
        return ''.join(res[::-1])