class Solution:
    def validSequence(self, w: str, p: str) -> List[int]:
        m = {}
        j = len(p) - 1
        for i in range(len(w) - 1, -1, -1):
            if j == -1:
                break
            if w[i] == p[j]:
                m[len(p) - j] = len(w) - i
                j -= 1
        def check(w, p):
            if len(p) in m:
                return m[len(p)] <= len(w)
            return len(p) == 0
        j = 0
        res = []
        for i in range(len(w)):
            if j == len(p):
                break
            if p[j] == w[i]:
                res.append(i)
                j += 1
            elif check(w[i+1:], p[j+1:]):
                res.append(i)
                l = []
                xj = j + 1
                for xi in range(i + 1, len(w)):
                    if xj == len(p):
                        break
                    if w[xi] == p[xj]:
                        xj += 1
                        l.append(xi)
                res.extend(l)
                return res
        if len(res) == len(p):
            return res
        return []