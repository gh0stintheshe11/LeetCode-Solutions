class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def fun(s):
            ans = -1
            last = defaultdict(int)
            for i, c in enumerate(s):
                last[c] = i
            finished = []
            first = defaultdict(int)
            for i in range(n - 1):
                c = s[i]
                if c not in first:
                    first[c] = i
                if i == last[c]:
                    finished.append(c)
                    for c in finished:
                        j = first[c]
                        if all((pf[c][i + 1] == pf[c][j] or pf[c][i + 1] - pf[c][j] == ct[c]) for c in ct):
                            ans = max(ans, i - j + 1)
            return ans

        n = len(s)
        ct = Counter(s)
        pf = {}
        for c in ct:
            pf[c] = [0]
        for i, c in enumerate(s):
            for t in ct:
                pf[t].append(pf[t][-1] + int(c == t))
        ans = fun(s)
        for c in pf:
            tot = ct[c]
            pf[c] = [tot - v for v in pf[c]]
            pf[c].reverse()
        return max(ans, fun(s[::-1]))