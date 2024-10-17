class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        que = []
        depths = {}
        for val in order:
            res = 0
            idx = bisect.bisect(que, val)
            if idx != 0:
                res = max(res, depths[que[idx - 1]])
            if idx != len(que):
                res = max(res, depths[que[idx]])
            que.insert(idx, val)
            depths[val] = res + 1
        return max(depths.values())