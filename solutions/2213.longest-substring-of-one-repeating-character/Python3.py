from sortedcontainers import SortedList

class Solution:
    def remove_seg(self, l, r):
        self.segs.remove((l, r))
        self.max_segs.remove((r-l, l, r))
        
    def add_seg(self, l, r):
        self.segs.add((l, r))
        self.max_segs.add((r-l, l, r))
        
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        self.segs = SortedList()
        self.max_segs = SortedList()
        l = 0
        for i in range(len(s)):
            if i and s[i] != s[i-1]:
                self.add_seg(l, i)
                l = i
        if l < len(s):
            self.add_seg(l, len(s))
        results = []
        for c, idx in zip(queryCharacters, queryIndices):
            if s[idx] == c:
                results.append(results[-1] if results else self.max_segs[-1][0])
                continue
            current = self.segs.bisect_left((idx, float('-inf')))
            if current == len(self.segs) or self.segs[current][0] > idx:
                current -= 1
            l, r = self.segs[current]
            self.remove_seg(l, r)
            if r - (idx + 1) > 0:
                self.add_seg(idx+1, r)
            if idx - l > 0:
                self.add_seg(l, idx)
                current += 1            
            if 0 < idx < len(s) - 1 and s[idx-1] == c == s[idx+1]:
                prev = self.segs[current - 1]
                succ = self.segs[current]
                self.remove_seg(prev[0], prev[1])
                self.remove_seg(succ[0], succ[1])
                self.add_seg(prev[0], succ[1])
            elif 0 < idx and s[idx-1] == c:
                prev = self.segs[current - 1]
                self.remove_seg(prev[0], prev[1])
                self.add_seg(prev[0], idx+1)
            elif idx < len(s) - 1 and s[idx+1] == c:
                succ = self.segs[current]
                self.remove_seg(succ[0], succ[1])
                self.add_seg(idx, succ[1])
            else:
                self.add_seg(idx, idx+1)
            s[idx] = c
            results.append(self.max_segs[-1][0])
        return results