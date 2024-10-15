from typing import List
from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index_map = defaultdict(list)
        
        for i, num in enumerate(arr):
            index_map[num].append(i)
        
        result = [0] * len(arr)

        for indices in index_map.values():
            n = len(indices)
            prefix_sum = [0] * (n + 1)

            for i in range(n):
                prefix_sum[i + 1] = prefix_sum[i] + indices[i]

            for i in range(n):
                left_distance = indices[i] * i - prefix_sum[i]
                right_distance = (prefix_sum[n] - prefix_sum[i + 1]) - indices[i] * (n - i - 1)
                result[indices[i]] = left_distance + right_distance

        return result