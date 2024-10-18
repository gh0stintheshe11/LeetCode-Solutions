from itertools import combinations
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hset = set((abs(a-b) for a, b in combinations(hFences + [1, m], 2)))
        vset = set((abs(a-b) for a, b in combinations(vFences + [1, n], 2)))
        inter = hset.intersection(vset)
        return (max(inter)**2)%(10**9 + 7) if inter else -1