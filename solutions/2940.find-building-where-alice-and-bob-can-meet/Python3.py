from typing import List, Optional, Callable
from bisect import bisect_left

class SegmentTree:
    def __init__(self, nums: List[int], identity_val: Optional[int], cmp: Callable, key: Callable = lambda x: x):
        self.n = len(nums)
        self.identity_val = identity_val
        self.key = key
        self.cmp = cmp

        self.nums = nums
        self.__build_nums()
        self.tree = [identity_val] * self.n * 2
        self.__build_tree()
    
    def __build_nums(self):
        self.nums = [self.key(x) for x in self.nums]

    def __build_tree(self):
        for i in range(self.n):
            self.tree[i + self.n] = self.nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.cmp(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index: int, val: int):
        index += self.n
        self.tree[index] = val
        while index > 1:
            new_val = self.cmp(self.tree[index], self.tree[index ^ 1])
            index //= 2
            if self.tree[index] == new_val:
                break
            self.tree[index] = new_val

    def query(self, left: int, right: int) -> int:
        res = self.identity_val
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                res = self.cmp(res, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = self.cmp(res, self.tree[right])
            left //= 2
            right //= 2
        return res

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        st = SegmentTree(heights, 0, lambda x, y: max(x, y))
        
        indexMap = {i: [] for i in heights}
        for i, x in enumerate(heights):
            indexMap[x].append(i)
        n = len(heights)
        
        res = []
        for a, b in queries:
            a, b = min(a, b), max(a, b)
            if heights[b] > heights[a] or a == b:
                res.append(b)
                continue
            
            ans = n
            l, r = b + 1, n
            if l == r:
                res.append(-1)
                continue
            maxR = st.query(l, r)
            while maxR > heights[a]:
                indexLoc = bisect_left(indexMap[maxR], l)
                r = indexMap[maxR][indexLoc]
                ans = r
                if l >= r:
                    break
                maxR = st.query(l, r)
            if ans == n:
                res.append(-1)
            else:
                res.append(ans)
        return res