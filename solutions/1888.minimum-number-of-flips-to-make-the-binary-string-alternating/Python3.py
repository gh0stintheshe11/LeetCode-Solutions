class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  # Duplicate the string to handle cyclic shifts.

        alt1, alt2 = '', ''
        for i in range(len(s)):
            if i % 2 == 0:
                alt1 += '0'
                alt2 += '1'
            else:
                alt1 += '1'
                alt2 += '0'

        min_flips = float('inf')
        diff1, diff2 = 0, 0
        for i in range(len(s)):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1
            
            if i >= n:
                if s[i - n] != alt1[i - n]:
                    diff1 -= 1
                if s[i - n] != alt2[i - n]:
                    diff2 -= 1

            if i >= n - 1:
                min_flips = min(min_flips, diff1, diff2)

        return min_flips