class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d = Counter(s)
        l = sorted(d.items(), key=lambda x:x[1])
        l = l[::-1]
        a = l[0][1]
        p = []
        for i in l:
            if d[i[0]] == a:
                p.append(i[0])
            else:
                break
        t = ""
        r = len(s) - 1
        while len(p) > 0:
            if s[r] in p:
                t += s[r]
                p.remove(s[r])
            else:
                r -= 1
        return t[::-1]