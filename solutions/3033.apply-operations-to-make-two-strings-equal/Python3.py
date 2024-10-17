class Solution:
    def getS(self, a, i, j, x):
        s = 0
        for i in range(i, j, 2):
            s += min(abs(a[i+1] - a[i]), x)
        return s
        
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        a = []
        for i in range(n):
            if s1[i] != s2[i]:
                a.append(i)
        n = len(a)
        if n == 0:
            return 0
        if n % 2 == 1:
            return -1
        for v in list(a):
            move = None
            gain = 0
            i = a.index(v)
            if i % 2 == 0:
                pre = min(x, abs(a[i] - a[i+1]))
                nex = 0
                for j in range(i-2, -1, -2):
                    pre += min(x, abs(a[j] - a[j+1]))
                    d = pre - nex
                    d -= min(x, abs(a[i] - a[j]))
                    d -= min(x, abs(a[i-1] - a[i+1]))
                    if d > gain:
                        gain = d
                        move = [i, j]
                    nex += min(x, abs(a[j] - a[j-1]))
                pre = min(x, abs(a[i] - a[i+1]))
                nex = 0
                for j in range(i+2, n, 2):
                    pre += min(x, abs(a[j] - a[j+1]))
                    nex += min(x, abs(a[j] - a[j-1]))
                    d = pre - nex
                    d -= min(x, abs(a[i] - a[j+1]))
                    if d > gain:
                        gain = d
                        move = [i, j]
            else:
                pre = min(x, abs(a[i] - a[i-1]))
                nex = 0
                for j in range(i-3, -1, -2):
                    pre += min(x, abs(a[j] - a[j+1]))
                    nex += min(x, abs(a[j+1] - a[j+2]))
                    d = pre - nex
                    d -= min(x, abs(a[i] - a[j]))
                    if d > gain:
                        gain = d
                        move = [i, j]
                pre = min(x, abs(a[i] - a[i-1]))
                nex = 0
                for j in range(i+1, n, 2):
                    pre += min(x, abs(a[j] - a[j+1]))
                    d = pre - nex
                    d -= min(x, abs(a[i] - a[j+1]))
                    d -= min(x, abs(a[i-1] - a[i+1]))
                    if d > gain:
                        gain = d
                        move = [i, j]
                    nex += min(x, abs(a[j] - a[j-1]))
            if gain == 0:
                continue
            a.insert(move[1], a.pop(move[0]))
        ans = self.getS(a, 0, n, x)
        return ans