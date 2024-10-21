def bisect_left(lst, num, lo=0, hi=None):
    if hi is None: hi = len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < num: lo = mid + 1
        else: hi = mid
    return lo

class Solution:
    def minReverseOperations(self, n: int, p: int, banned_: List[int], k: int) -> List[int]:
        banned = set(banned_)
        lists = [[], []]
        pos = [(0 if i == p else -1) for i in range(n)]
        for i in range(n):
            if i in banned or i == p:
                continue
            lists[i % 2].append(i)
        queue = [p]

        for i in queue:
            l = lists[(k - 1 - i) % 2]
            lower_min = max(0, i - k + 1)
            lower_max = min(n - k, i)
            j_lower_min = 2 * lower_min + k - 1 - i
            j_lower_max = 2 * lower_max + k - 1 - i
            j = bisect_left(l, j_lower_min)
            while j < len(l) and l[j] <= j_lower_max:
                queue.append(l[j])
                pos[l[j]] = pos[i] + 1
                del l[j]

        return pos