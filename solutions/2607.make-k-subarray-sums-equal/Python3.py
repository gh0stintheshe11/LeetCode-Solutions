from typing import List
from collections import defaultdict
import math

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        gcd_k_n = math.gcd(n, k)
        groups = defaultdict(list)

        for i in range(n):
            groups[i % gcd_k_n].append(arr[i])
        
        def min_operations_to_median(group: List[int]) -> int:
            group.sort()
            median = group[len(group) // 2]
            return sum(abs(x - median) for x in group)
        
        operations = 0
        for group in groups.values():
            operations += min_operations_to_median(group)

        return operations