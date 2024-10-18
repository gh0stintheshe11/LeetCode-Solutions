class Solution:
    def numberOfStableArrays(self, z: int, o: int, lim: int) -> int:
        n = z + o
        f = [[0] * n for _ in range(n + 1)]
        g = [[0] * n for _ in range(n + 1)]
        s = [[0] * (n + 1) for _ in range(n + 1)]
        t = [[0] * (n + 1) for _ in range(n + 1)]
        f[0][0] = s[0][1] = 1
        g[0][0] = t[0][1] = 1
        for i in range(1, n):
            for j in range(i + 1):
                if i - o < j <= z:
                    f[j][i] = (t[i - j][i] - t[i - j][max(0, i - lim)] + 1000000007) % 1000000007
                s[j][i + 1] = (s[j][i] + f[j][i]) % 1000000007
                if i - z < j <= o:
                    g[j][i] = (s[i - j][i] - s[i - j][max(0, i - lim)] + 1000000007) % 1000000007
                t[j][i + 1] = (t[j][i] + g[j][i]) % 1000000007
        return (sum(f[z][i] for i in range(max(z, n - lim), n)) + 
                sum(g[o][i] for i in range(max(o, n - lim), n))) % 1000000007