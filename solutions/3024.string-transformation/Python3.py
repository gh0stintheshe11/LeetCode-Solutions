class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10**9 + 7

        n = len(s)
        # similar to fibonacci explicit formula: https://www.youtube.com/watch?v=DxJe-9QU0vk&ab_channel=Zak%27sLab
        def f(k_):
            return (pow(n-1, k_, MOD) - pow(-1, k_)) * pow(n, -1, MOD)
    
        ans = 0
        if s == t:
            ans += (n-1) * f(k-1)
        cnt = self.kmp(t[1:] + t[:-1], s)
        ans += cnt * f(k)
        return ans % MOD

    # ----
    # the rest is KMP
    # https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    def kmp(self, text, word):
        cnt = 0
        z = self.calc_z(word)
        i = 0
        j = 0
        while i < len(text):
            if word[j] != text[i]:
                j = z[j]
                if j < 0:
                    i += 1
                    j += 1
                continue
            i += 1
            j += 1
            if j == len(word):
                cnt += 1
                j = z[j]
        return cnt
    
    def calc_z(self, s):
        z = [None for _ in range(len(s)+1)]
        z[0] = -1
        i = 1
        j = 0
        
        while i < len(s):
            if s[i] == s[j]:
                z[i] = z[j]
            else:
                z[i] = j
                while j >= 0 and s[i] != s[j]:
                    j = z[j]
            i += 1
            j += 1
        z[i] = j
        return z