from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        remaining = list([i for i in range(1, n)])
        ans = []

        for x, y in queries:
            l = bisect_right(remaining, x)
            r = bisect_left(remaining, y)
            for i in range(l, r):
                remaining.pop(l)
            ans.append(len(remaining))

        return ans