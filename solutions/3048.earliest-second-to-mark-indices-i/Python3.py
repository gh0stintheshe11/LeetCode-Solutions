class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        if len(set(changeIndices)) < n or sum(nums) + n > m:
            return -1
        indices = [list() for _ in range(n+1)]
        for i, v in enumerate(changeIndices):
            indices[v].append(i)

        for end in range(sum(nums) + n - 1, m):
            last_indices = []
            for v in range(1, n+1):
                idx = bisect.bisect_right(indices[v], end) - 1
                if idx < 0:
                    break
                last_indices.append(indices[v][idx])
            if len(last_indices) < n:
                continue
            last_indices.sort()
            s = 0
            for idx in last_indices:
                if idx < s + nums[changeIndices[idx]-1]:
                    break
                s += nums[changeIndices[idx]-1] + 1
            else:
                return end + 1
        return -1