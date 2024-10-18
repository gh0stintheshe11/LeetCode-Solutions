import heapq
from collections import defaultdict

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        res = []
        min_heap = []  # [freq, char]
        d = defaultdict(int)
        replaced_chars = []

        for i in 'abcdefghijklmnopqrstuvwxyz':
            d[i] = 0

        for i in s:
            if i != '?':
                d[i] += 1

        for i in d:
            heapq.heappush(min_heap, [d[i], i])

        for i in s:
            if i == '?':
                freq, char = heapq.heappop(min_heap)
                replaced_chars.append(char)
                heapq.heappush(min_heap, [freq + 1, char])

        replaced_chars.sort()
        j = 0
        for i in range(len(s)):
            if s[i] == '?':
                res.append(replaced_chars[j])
                j += 1
            else:
                res.append(s[i])

        return ''.join(res)