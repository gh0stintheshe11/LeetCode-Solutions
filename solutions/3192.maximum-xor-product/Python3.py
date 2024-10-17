class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        z = 0
        for x in range(n-1, -1, -1):
            t = z | (1 << x)
            if ((a >> x) & 1 == (b >> x) & 1):
                if ((a >> x) & 1 == 0):
                    z = t
            else:
                if ((a ^ t) * (b ^ t) > (a ^ z) * (b ^ z)):
                    z = t       
        return (a ^ z) * (b ^ z) % 1000000007