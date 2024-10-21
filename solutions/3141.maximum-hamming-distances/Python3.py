class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        snums = set(nums)
        graph = {i: set([]) for i in range(2**m)}
        for i in range(2**m):
            for j in range(m):
                mask = 1 << j
                if i & mask:
                    graph[i].add(i - mask)
                else:
                    graph[i].add(i + mask)
        resdict = {i: 0 for i in range(2**m)}
        antis = [n ^ (2**m - 1) for n in snums]
        queue = []
        seen = set([])
        for a in antis:
            queue.append((a, 0))
            seen.add(a)
        for n, d in queue:
            resdict[n] = d
            for ns in graph[n]:
                if ns not in seen:
                    seen.add(ns)
                    queue.append((ns, d + 1))
        return [m - resdict[a] for a in nums]