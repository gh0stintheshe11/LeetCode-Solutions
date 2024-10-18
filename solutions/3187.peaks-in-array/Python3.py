class SegmentTree:
    def __init__(self, n, nums):
        self.seg = [0] * (4 * n)
        self.n = n
        self.nums = nums
        self.build(0, 0, n - 1)

    def build(self, ind, low, high):
        if low == high:
            self.seg[ind] = 1 if self.is_peak(low) else 0
            return
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid)
        self.build(2 * ind + 2, mid + 1, high)
        self.seg[ind] = self.seg[2 * ind + 1] + self.seg[2 * ind + 2]

    def query(self, ind, low, high, gl, gh):
        if gl <= low and gh >= high:
            return self.seg[ind]
        if gl > high or gh < low:
            return 0

        mid = (low + high) // 2
        lft = self.query(2 * ind + 1, low, mid, gl, gh)
        rgt = self.query(2 * ind + 2, mid + 1, high, gl, gh)
        return lft + rgt

    def update(self, ind, low, high, k):
        if low == high:
            self.seg[ind] = 1 if self.is_peak(low) else 0
            return
        mid = (low + high) // 2
        if k <= mid:
            self.update(2 * ind + 1, low, mid, k)
        else:
            self.update(2 * ind + 2, mid + 1, high, k)
        self.seg[ind] = self.seg[2 * ind + 1] + self.seg[2 * ind + 2]

    def is_peak(self, i):
        if i <= 0 or i >= self.n - 1:
            return False
        return self.nums[i] > self.nums[i - 1] and self.nums[i] > self.nums[i + 1]


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = SegmentTree(n, nums)
        ans = []

        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                ans.append(seg_tree.query(0, 0, n - 1, l + 1, r - 1))
            elif query[0] == 2:
                idx, val = query[1], query[2]
                nums[idx] = val
                for i in range(max(0, idx - 1), min(n, idx + 2)):
                    seg_tree.update(0, 0, n - 1, i)

        return ans