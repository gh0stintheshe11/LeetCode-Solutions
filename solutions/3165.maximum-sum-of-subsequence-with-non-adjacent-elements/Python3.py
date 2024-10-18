class Node:
    def __init__(self, lo, hi, nums):
        self.lo = lo
        self.hi = hi
        self.selected = [[0]*2 for _ in range(2)]
        if lo < hi:
            mid = (lo + hi)//2
            self.l = Node(lo, mid, nums)
            self.r = Node(mid+1, hi, nums)
            self.combine()
        else:
            self.selected[0][0] = 0
            self.selected[0][1] = float('-inf')
            self.selected[1][0] = float('-inf')
            self.selected[1][1] = nums[lo]
    
    def combine(self):
        self.selected[0][0] = max(self.l.selected[0][0]+self.r.selected[0][0], self.l.selected[0][1]+self.r.selected[0][0], self.l.selected[0][0]+self.r.selected[1][0])
        self.selected[0][1] = max(self.l.selected[0][0]+self.r.selected[0][1], self.l.selected[0][1]+self.r.selected[0][1], self.l.selected[0][0]+self.r.selected[1][1])
        self.selected[1][0] = max(self.l.selected[1][0]+self.r.selected[0][0], self.l.selected[1][1]+self.r.selected[0][0], self.l.selected[1][0]+self.r.selected[1][0])
        self.selected[1][1] = max(self.l.selected[1][0]+self.r.selected[0][1], self.l.selected[1][1]+self.r.selected[0][1], self.l.selected[1][0]+self.r.selected[1][1])
    
    def update(self, i, x):
        if i < self.lo or self.hi < i: return 
        if self.lo == self.hi:
            self.selected[0][0] = 0
            self.selected[1][1] = x
            return
        self.l.update(i, x)
        self.r.update(i, x)
        self.combine()

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        tree = Node(0, len(nums)-1, nums)
        res = 0
        MOD = 10**9+7
        for i, x in queries:
            tree.update(i, x)
            res += max(max(tree.selected[0]), max(tree.selected[1]))
            res %= MOD
        return res