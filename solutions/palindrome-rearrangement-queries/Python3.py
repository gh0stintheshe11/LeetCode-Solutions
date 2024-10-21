class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        m = n // 2
        nq = len(queries)
        s1, s2 = s[:m], s[m:][::-1]
        if Counter(s1) != Counter(s2): 
            return [False] * nq

        pf1 = [[0] * (m + 1) for _ in range(26)]
        pf2 = [[0] * (m + 1) for _ in range(26)]
        dif = [0] * (m + 1)
        l, r = n, -1
        c2i = {chr(ord('a') + i): i for i in range(26)}
        for i in range(n // 2):
            i1 = c2i[s1[i]]
            i2 = c2i[s2[i]]
            for j in range(26):
                pf1[j][i] = pf1[j][i - 1] + (i1 == j)
                pf2[j][i] = pf2[j][i - 1] + (i2 == j)
            dif[i] = dif[i - 1]
            if i1 != i2:
                dif[i] += 1
                l = min(l, i)
                r = max(l, i)
        if l == n:
            return [True] * nq

        def check(a, b, c, d, ps1, ps2):
            le = c - 1
            if c > b:
                if dif[c - 1] - dif[b]:
                    return False
                le = b
            for i in range(26):
                if ps1[i][b] - ps1[i][a - 1] < ps2[i][le] - ps2[i][a - 1]:
                    return False
            return True
        
        ans = []
        for a, b, c, d in queries:
            c, d = n - 1 - d, n - 1 - c
            if c < a or (c == a and d >= b):
                a, b, c, d = c, d, a, b
                ps1, ps2 = pf2, pf1
            else:
                ps1, ps2 = pf1, pf2
            
            if (a <= l and b >= r):
                ans.append(True)
                continue
            
            if a > l or max(b, d) < r:
                ans.append(False)
                continue

            ans.append(check(a, b, c, d, ps1, ps2))
        
        return ans