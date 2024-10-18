class SegNode:
    def __init__(self, l, r, val=0, left=None, right=None):
        self.l, self.r, self.val = l, r, val
        self.left, self.right = left, right

class SegTree:
    def __init__(self, size):
        self.root = SegNode(0, size)

    def update(self, n, index, val):
        if n.l == n.r:
            n.val = max(n.val, val)
            return
        mid = (n.l + n.r) // 2
        n.left = n.left or SegNode(n.l, (n.l + n.r) // 2)
        n.right = n.right or SegNode((n.l + n.r) // 2 + 1, n.r)
        if index <= mid:
            self.update(n.left, index, val)
        else:
            self.update(n.right, index, val)
        n.val = max(n.left.val, n.right.val)

    def query(self, l, r, n):
        if n.r < l or r < n.l:
            return 0
        if l <= n.l and r >= n.r:
            return n.val
        n.left = n.left or SegNode(n.l, (n.l + n.r) // 2)
        n.right = n.right or SegNode((n.l + n.r) // 2 + 1, n.r)
        a = self.query(l, r, n.left)
        b = self.query(l, r, n.right)
        return max(a, b)

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        x, y = coordinates[k]
        size, ans = max(c for _, c in coordinates), 0
        tree = SegTree(size)
        for r, c in sorted(coordinates, key=lambda x: (x[0], -x[1])):
            if (r <= x and c <= y) or (x < r and y < c):
                n = tree.query(0, c - 1, tree.root)
                tree.update(tree.root, c, n + 1)
                ans = max(ans, n)
        return ans + 1