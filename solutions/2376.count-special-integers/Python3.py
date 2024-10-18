class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, tight, mask, leadingZero):
            if i == len(digits):
                return 1

            maxDigit = 9
            if tight:
                maxDigit = digits[i]

            ans = 0
            for d in range(maxDigit + 1):
                nxtTight = tight and d == maxDigit
                nxtLeadingZero = leadingZero and d == 0
                if (mask >> d) & 1: continue
                newMask = mask
                if not nxtLeadingZero:
                    newMask = mask ^ (1 << d)

                ans += dp(i+1, nxtTight, newMask, nxtLeadingZero)
            return ans

        return dp(0, True, 0, True) - 1