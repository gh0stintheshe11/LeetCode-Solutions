from typing import List
from collections import namedtuple
from itertools import accumulate

SearchResult = namedtuple('SearchResult', 'points,cost')

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        
        nums = [0] + nums + [0]
        N = len(nums)
        marked = []
        bisect_memo = [0] * N
        for i, x in enumerate(nums):
            bisect_memo[i] = len(marked)
            if 1 == x:
                marked.append(i)
                
        if 0 == len(marked):
            return k * 2  # we can only apply rule1 for all the points

        # make the prefix memo
        presum = [0] + list(accumulate(marked))

        def calcCost(lidx, ii, ptNeeded):
            iidx = bisect_memo[ii]
            if lidx > iidx:
                lidx = iidx
            ridx = min(lidx + ptNeeded - 1, len(marked) - 1)
            points = (ridx + 1) - lidx
            if points < ptNeeded:
                return SearchResult(0, 0)

            cost = 0
            lpt = iidx - lidx
            assert(lpt >= 0)
            cost += lpt * ii - (presum[iidx] - presum[lidx])
            if ridx >= iidx:
                rpt = (ridx + 1) - iidx
                assert(rpt >= 0)
                cost += (presum[ridx + 1] - presum[iidx]) - rpt * ii
            return SearchResult(points, cost)

        def cntSet(ii, ptNeeded):
            # calculate number of items set between i-mid to i+mid
            more = ptNeeded - nums[ii]
            mid = (more >> 1) + (more & 1)

            iidx = bisect_memo[ii]

            lidx = max(0, iidx - mid)
            ridx = min(lidx + ptNeeded - 1, len(marked) - 1)
            points = (ridx + 1) - lidx
            if points < ptNeeded:
                lidx = max(0, ridx - ptNeeded + 1)

            ptA, costA = calcCost(lidx, ii, ptNeeded)
            ptB, costB = calcCost(lidx + 1, ii, ptNeeded)

            if ptA != ptNeeded:
                ptA, costA = ptB, costB
            
            if ptB == ptNeeded:
                costA = min(costA, costB)

            if ptA < ptNeeded:
                return SearchResult(0, 0)
            return SearchResult(ptA, costA)
        
        INF = float('Inf')
        result = N * k
        for i in range(1, N - 1):
            kk, ct = k, 0
            kk -= nums[i]
            if 0 == kk:
                return ct
            kk -= nums[i - 1]
            ct += nums[i - 1]
            if 0 == kk:
                return ct
            kk -= nums[i + 1]
            ct += nums[i + 1]
            appl = min(kk, maxChanges)
            kk -= appl
            ct += appl * 2
            if 0 == kk:
                assert(ct >= 0)
                result = min(result, ct)
            else:
                assert(kk > 0)
                kk, ct = k, 0
                kk -= appl
                ct += appl * 2
                res = cntSet(i, kk)
                assert(res.cost >= 0)
                assert(ct >= 0)
                if res.points == kk:
                    result = min(result, res.cost + ct)
        return result