from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for a, b in allowedSwaps:
            union(a, b)
        
        component_map = defaultdict(list)
        for i in range(len(source)):
            component_map[find(i)].append(i)
        
        min_hamming_distance = 0
        for indices in component_map.values():
            source_count = Counter(source[i] for i in indices)
            target_count = Counter(target[i] for i in indices)
            for key in source_count:
                if key in target_count:
                    min_hamming_distance += max(0, source_count[key] - target_count[key])
                else:
                    min_hamming_distance += source_count[key]
        
        return min_hamming_distance