from typing import List
import bisect

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def minOperationsToMakeNonDecreasing(subsequence):
            lis = []
            for num in subsequence:
                idx = bisect.bisect_right(lis, num)
                if idx == len(lis):
                    lis.append(num)
                else:
                    lis[idx] = num
            return len(subsequence) - len(lis)
        
        min_operations = 0
        for start in range(k):
            subsequence = arr[start::k]
            min_operations += minOperationsToMakeNonDecreasing(subsequence)
        
        return min_operations