from typing import List
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt_x = [0] * (mx + 1)
        for x in nums:
            cnt_x[x] += 1
            
        cnt_gcd = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            c = 0
            for j in range(i, mx + 1, i):
                c += cnt_x[j]
                cnt_gcd[i] -= cnt_gcd[j]
            cnt_gcd[i] += c * (c - 1) // 2

        s = list(accumulate(cnt_gcd))
        return [bisect_right(s, q) for q in queries]