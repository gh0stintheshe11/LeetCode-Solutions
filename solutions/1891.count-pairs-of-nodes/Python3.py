from collections import defaultdict, Counter
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * (n + 1)
        shared = defaultdict(int)

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if u > v:
                u, v = v, u
            shared[(u, v)] += 1

        result = []
        for query in queries:
            total_pairs = 0
            count = Counter(degree[1:])
            degrees = sorted(degree[1:])

            j = len(degrees) - 1
            possible_pairs = 0
            for i in range(len(degrees)):
                while j > i and degrees[i] + degrees[j] > query:
                    possible_pairs += j - i
                    j -= 1

            total_pairs += possible_pairs

            for (u, v), cnt in shared.items():
                if degree[u] + degree[v] > query and degree[u] + degree[v] - cnt <= query:
                    total_pairs -= 1
            
            result.append(total_pairs)
            
        return result