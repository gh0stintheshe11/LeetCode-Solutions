class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(part):
            return int(part) <= 255 if len(part) == 1 or (part[0] != '0' and int(part) > 0) else False

        def restore(s, k, path, res):
            if s and k == 0 and is_valid(s):
                res.append(path + s)
            elif k > 0:
                for i in range(min(3, len(s))):
                    part = s[:i+1]
                    if is_valid(part):
                        restore(s[i+1:], k-1, path+ part + '.', res)

        res = []
        restore(s, 3, '', res)
        return res