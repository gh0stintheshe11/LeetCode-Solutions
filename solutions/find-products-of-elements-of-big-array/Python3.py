def getcount(n, k):
    n += 1
    res = (n >> (k + 1)) << k
    if (n >> k) & 1:
        res += n & ((1 << k) - 1)
    return res

def gettotal(n):
    res = 0
    for b in range(60):
        res += getcount(n, b)
    return res

class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        res = []
        for f, t, mod in queries:
            beg = 1
            end = 10 ** 15
            l = r = 0
            while beg <= end:
                mid = (beg + end) // 2
                if gettotal(mid - 1) >= f:
                    l = mid
                    end = mid - 1
                else:
                    beg = mid + 1
            beg = 1
            end = 10 ** 15
            while beg <= end:
                mid = (beg + end) // 2
                if gettotal(mid) - 1 <= t:
                    r = mid
                    beg = mid + 1
                else:
                    end = mid - 1
            s = 0
            for b in range(60):
                if l > r:
                    continue
                s += b * (getcount(r, b) - getcount(l - 1, b))
            curr = pow(2, s, mod)
            val = l - 1
            pos = gettotal(val - 1)
            pw = 1
            while val:
                if val & 1:
                    if f <= pos <= t:
                        curr *= pw
                        curr %= mod
                    pos += 1
                pw *= 2
                val //= 2
            if r + 1 != l - 1:
                val = r + 1
                pos = gettotal(val - 1)
                pw = 1
                while val:
                    if val & 1:
                        if f <= pos <= t:
                            curr *= pw
                            curr %= mod
                        pos += 1
                    pw *= 2
                    val //= 2
            res.append(curr)
        return res