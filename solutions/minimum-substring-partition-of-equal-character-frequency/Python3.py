class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        def isBalancedSubstring(hs):
            pre = 0
            for v in hs.values():
                if pre == 0:
                    pre = v
                elif pre != v:
                    return False
            return True

        @cache
        def check(i):
            if i >= n:
                return 0
            res, count = n, {}
            if i < n:
                for j in range(i, n):
                    count[s[j]] = count.get(s[j], 0) + 1
                    if isBalancedSubstring(count):
                        res = min(res, 1 + check(j+1))
            return res

        return check(0)