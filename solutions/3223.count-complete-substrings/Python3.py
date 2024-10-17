class Solution:
    def countCompleteSubstrings(self, w: str, k: int) -> int:
        def calc(s):
            res = 0
            v = len(s)
            for i in range(1, 27):
                if i * k > v: break
                l = i * k
                
                cnt = Counter()
                left = 0

                for right in range(len(s)):
                    cnt[s[right]] += 1
                    if right - left + 1 == l:
                        for val in cnt.values():
                            if val > k:
                                break
                        else:
                            if len(cnt) == i:
                                res += 1
                        cnt[s[left]] -= 1
                        if cnt[s[left]] == 0:
                            del cnt[s[left]]
                        left += 1
            return res
        
        idx = 0
        ans = 0
        n = len(w)
        for i in range(1, n):
            if abs(ord(w[i]) - ord(w[i-1])) > 2:
                ans += calc(w[idx:i])
                idx = i
        ans += calc(w[idx:])
        return ans