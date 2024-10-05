class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        m, n = len(stamp), len(target)
        s, t = list(stamp), list(target)
        res = []
        total_stamp, turn_stamp = [False] * n, True
        
        def can_stamp(i):
            changed = False
            for j in range(m):
                if t[i + j] == '*':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i:i + m] = ['*'] * m
                res.append(i)
            return changed
        
        while turn_stamp:
            turn_stamp = False
            for i in range(n - m + 1):
                if can_stamp(i):
                    turn_stamp = True
        
        return res[::-1] if t == ['*'] * n else []