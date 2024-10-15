class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        n = len(s)
        l = 0
        seen = set()
        result = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            result += r - l + 1

        return result