from collections import deque
from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def possible(mid):
            n = len(lis)
            q = deque()
            ct = 0
            sumi = 0
            for i in range(n - 1):
                while q and abs(q[0][0] - i) > r:
                    a, b = q.popleft()
                    sumi -= b
                
                if lis[i] + sumi < mid:
                    q.append((i + r, mid - lis[i] - sumi))
                    ct += mid - lis[i] - sumi
                    sumi += mid - lis[i] - sumi
                if ct > k:
                    return 0
            return 1

        n = len(stations)
        lis = [0] * (n + 1)
        for i in range(n):
            lis[max(0, i - r)] += stations[i]
            lis[min(n, i + r + 1)] -= stations[i]
        for i in range(1, n + 1):
            lis[i] += lis[i - 1]
        lo = 0
        hi = 10**18
        output = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                output = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return output