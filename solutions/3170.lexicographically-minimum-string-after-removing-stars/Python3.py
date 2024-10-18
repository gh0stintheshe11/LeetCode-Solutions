from collections import defaultdict, OrderedDict

class Solution:
    def clearStars(self, s: str) -> str:
        mp = defaultdict(list)
        n = len(s)
        v = [0] * n

        for i in range(n):
            if s[i] != '*':
                mp[s[i]].append(i)
            else:
                v[i] = 1
                sorted_mp = OrderedDict(sorted(mp.items()))
                for key in list(sorted_mp.keys()):
                    idx_list = sorted_mp[key]
                    v[idx_list[-1]] = 1
                    idx_list.pop()
                    if not idx_list:
                        del mp[key]
                    break

        ans = ""
        for i in range(n):
            if v[i] != 1:
                ans += s[i]
                
        return ans