from math import log2
from typing import List

class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        self.st = [[0] * (int(log2(n)) + 1) for _ in range(n)]

        for i in range(n):
            self.st[i][0] = nums[i]

        p = 1
        while (1 << p) <= n:
            i = 0
            while i + (1 << p) <= n:
                self.st[i][p] = self.st[i][p - 1] & self.st[i + (1 << p - 1)][p - 1]
                i += 1
            p += 1

    def query(self, l, r):
        p = int(log2(r - l + 1))
        return self.st[l][p] & self.st[r - (1 << p) + 1][p]

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ST = SparseTable(nums)

        def bs_left(i, l, k):
            r = n
            while l < r:
                mid = (l + r) >> 1
                if ST.query(i, mid) > k:
                    l = mid + 1
                else:
                    r = mid

            return l

        cnt = 0
        for i in range(n):
            r1 = bs_left(i, i, k)
            if r1 < n and ST.query(i, r1) == k:
                r2 = bs_left(i, r1, k - 1) - 1
                cnt += r2 - r1 + 1

        return cnt