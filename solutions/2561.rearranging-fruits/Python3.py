from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        s = set(basket1) | set(basket2)
        tochange1 = []
        tochange2 = []
        for a in s:
            if (freq1[a] + freq2[a]) % 2 == 1:
                return -1
            if freq1[a] > freq2[a]:
                tochange1 += [a] * ((freq1[a] - freq2[a]) // 2)
            elif freq2[a] > freq1[a]:
                tochange2 += [a] * ((freq2[a] - freq1[a]) // 2)
        tochange1.sort()
        tochange2.sort(reverse=True)
        res = 0
        ms = min(s)
        for a, b in zip(tochange1, tochange2):
            res += min([a, b, ms * 2])
        return res