class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x : x[1])
        out = [0] * len(queries)
        hashmap = {}
        for i, query in enumerate(queries):
            hashmap[query] = i
        queries.sort()
        head, tail = 0, 0
        servers = set()
        seen = defaultdict(int)
        for query in queries:
            left, right = query - x, query
            while head < len(logs) and logs[head][1] < left:
                if logs[head][0] in seen:
                    seen[logs[head][0]] -= 1
                    if seen[logs[head][0]] == 0:
                        del seen[logs[head][0]]
                head += 1
            tail = max(tail, head)
            while tail < len(logs) and left <= logs[tail][1] <= right:
                seen[logs[tail][0]] += 1
                tail += 1
            out[hashmap[query]] = n - len(seen)
            
        return out