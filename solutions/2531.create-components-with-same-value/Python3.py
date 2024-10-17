class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        overall_total = sum(nums)
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(v=0, parent=-1):
            nonlocal overall_total
            res = {}
            total = nums[v]
            for u in graph[v]:
                if u != parent:
                    r = dfs(u, v)
                    k = next(iter(r.keys()))
                    total += r[k][0] * k + r[k][1]
                    for k in r:
                        if overall_total % k != 0:
                            continue
                        if k not in res:
                            res[k] = [r[k][0], r[k][1], 1]
                        else:
                            res[k][0] += r[k][0]
                            res[k][1] += r[k][1]
                            res[k][2] += 1
            
            solutions = {total: (1, 0)}
            for k in res:
                if overall_total % k != 0:
                    continue
                remains = total - (k * res[k][0])
                if remains == k:
                    solutions[k] = (res[k][0] + 1, 0)
                elif remains < k:
                    solutions[k] = (res[k][0], remains)
            return solutions

        ans = dfs()
        k = min(k for k, v in ans.items() if v[1] == 0)
        return ans[k][0] - 1