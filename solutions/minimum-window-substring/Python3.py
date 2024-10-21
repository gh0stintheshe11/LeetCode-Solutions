class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        counter_t = Counter(t)
        counter_s = {}
        left = right = 0
        min_len = float('inf')
        min_window = ''
        
        while right < len(s):
            if s[right] in counter_t:
                counter_s[s[right]] = counter_s.get(s[right], 0) + 1
                while all(map(lambda c: counter_s.get(c, 0) >= counter_t[c], counter_t.keys())):
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        min_window = s[left:right+1]
                    if s[left] in counter_s:
                        counter_s[s[left]] -= 1
                    left += 1
            right += 1
            
        return min_window