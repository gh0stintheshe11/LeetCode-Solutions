class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        
        @lru_cache(None)
        def changes(index, ll):
            mi = 20000
            for d in range(1, ll//2 + 1):
                if ll%d == 0:
                    arr = ['' for i in range(d)]
                    for j in range(index, min(len(s), index + ll)):
                        arr[j%d] += s[j]
                    cha = 0
                    for st in arr:
                        x=0
                        y = len(st) - 1
                        while x < y:
                            cha += st[x] != st[y]
                            x += 1
                            y -= 1
                    mi = min(mi, cha)
            return mi
        
        @lru_cache(None)
        def dfs(index, remain):
            if index >= len(s) and remain == 0:
                return 0
            if index >= len(s) or remain <= 0:
                return 10000
            ans = 10000
            ll=2
            while index + ll <= len(s):
                ans = min(ans, changes(index, ll) + dfs(index + ll, remain - 1))
                ll += 1
            return ans
        
        return dfs(0, k)