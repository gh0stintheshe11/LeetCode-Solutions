class Solution:
    def countSteppingNumbers(self, low: str, hi: str) -> int:
        mod = 10**9 + 7
        def solve(high):
            @cache 
            def dp(idx, tight, last, nz):
                if idx == len(high): return 1
                ans = 0
                h = 10 if not tight else int(high[idx]) + 1
                for i in range(h):
                    if not nz or abs(i - last) == 1: 
                        ans += dp(idx + 1, 1 if (tight and i == int(high[idx])) else 0, i, nz | (i != 0))
                    ans %= mod
                return ans
            return dp(0, 1, 0, 0)
        return (solve(hi) - solve(str(int(low) - 1))) % mod