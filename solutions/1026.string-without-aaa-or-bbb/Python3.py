class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if a > b:
                if a > 1:
                    res.append('aa')
                    a -= 2
                else:
                    res.append('a')
                    a -= 1
                if b > 0:
                    res.append('b')
                    b -= 1
            elif b > a:
                if b > 1:
                    res.append('bb')
                    b -= 2
                else:
                    res.append('b')
                    b -= 1
                if a > 0:
                    res.append('a')
                    a -= 1
            else:
                if a > 0:
                    res.append('a')
                    a -= 1
                if b > 0:
                    res.append('b')
                    b -= 1
        return ''.join(res)