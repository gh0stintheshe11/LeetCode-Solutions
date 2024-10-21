from collections import defaultdict
from functools import cache
from typing import List

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        
        @cache
        def diff(i, k):
            res = defaultdict(int)
            if k == 2:
                for j in range(i):
                    res[abs(nums[i]-nums[j])] += 1
            else:            
                for j in range(k-2, i):
                    cur_diff = abs(nums[i] - nums[j])
                    dic = diff(j, k-1)
                    for min_diff, count in dic.items():
                        res[min(cur_diff, min_diff)] += count
            return res
        
        res = 0
        for i in range(k-1, n):
            dic = diff(i, k)
            for min_diff, count in dic.items():
                res += min_diff * count
                res %= MOD
        return res