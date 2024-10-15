from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            pos = bisect.bisect_left(arr2, num)
            if (pos == 0 or num - arr2[pos - 1] > d) and (pos == len(arr2) or arr2[pos] - num > d):
                count += 1
        return count