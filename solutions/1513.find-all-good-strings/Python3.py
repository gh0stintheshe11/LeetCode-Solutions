class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        
        def buildKMP(pattern):
            kmp = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = kmp[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                kmp[i] = j
            return kmp
        
        kmp = buildKMP(evil)
        
        @lru_cache(None)
        def dp(pos, matchEvil, lessS1, lessS2):
            if matchEvil == len(evil):
                return 0
            if pos == n:
                return 1
            
            start = s1[pos] if not lessS1 else 'a'
            end = s2[pos] if not lessS2 else 'z'
            
            count = 0
            for c in range(ord(start), ord(end) + 1):
                ch = chr(c)
                
                newMatchEvil = matchEvil
                while newMatchEvil > 0 and ch != evil[newMatchEvil]:
                    newMatchEvil = kmp[newMatchEvil - 1]
                if ch == evil[newMatchEvil]:
                    newMatchEvil += 1
                
                count += dp(pos + 1, newMatchEvil, lessS1 or ch > s1[pos], lessS2 or ch < s2[pos])
                count %= MOD
            
            return count
        
        return dp(0, 0, False, False)