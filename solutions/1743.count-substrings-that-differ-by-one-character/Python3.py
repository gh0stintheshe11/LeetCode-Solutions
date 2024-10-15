class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def count_diff_by_one(i, j):
            count = 0
            mismatch = 0
            res = 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    mismatch += 1
                if mismatch == 1:
                    res += 1
                elif mismatch > 1:
                    break
                i += 1
                j += 1
            return res
        
        answer = 0
        for i in range(len(s)):
            for j in range(len(t)):
                answer += count_diff_by_one(i, j)
        
        return answer