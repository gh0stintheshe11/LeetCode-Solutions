class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict

        degree_count = [0] * (n + 1)
        pairs = defaultdict(set)

        for u, v in edges:
            degree_count[u] += 1
            degree_count[v] += 1
            pairs[u].add(v)
            pairs[v].add(u)

        odd_degree_nodes = [i for i in range(1, n + 1) if degree_count[i] % 2 == 1]

        if len(odd_degree_nodes) == 0:
            return True
        if len(odd_degree_nodes) == 2:
            a, b = odd_degree_nodes
            if b not in pairs[a]:
                return True
            for i in range(1, n + 1):
                if i != a and i != b and i not in pairs[a] and i not in pairs[b]:
                    return True
            return False
        if len(odd_degree_nodes) == 4:
            a, b, c, d = odd_degree_nodes
            if (b not in pairs[a] and d not in pairs[c]) or (c not in pairs[a] and d not in pairs[b]) or (d not in pairs[a] and c not in pairs[b]):
                return True
        return False