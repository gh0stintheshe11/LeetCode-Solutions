from typing import List
from bisect import bisect_left

class Node:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        if l == r:
            self.value = -1
        else:
            mid = (l + r) // 2
            self.left = Node(l, mid)
            self.right = Node(mid + 1, r)
            self.value = max(self.left.value, self.right.value)
    
    def find(self, l: int, r: int) -> int:
        if self.l > r or self.r < l: return -1
        elif l <= self.l and self.r <= r: return self.value
        else:
            return max(self.left.find(l, r), self.right.find(l, r))
    
    def update(self, idx: int, value):
        if self.l > idx or self.r < idx: return 
        elif idx == self.l == self.r: 
            self.value = value
        else:
            self.left.update(idx, value)
            self.right.update(idx, value)
            self.value = max(self.left.value, self.right.value)
        
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums1)
        M = len(queries)
        
        # order according to nums1 
        arr1 = [(nums1[i], nums2[i]) for i in range(N)]
        arr1.sort()
        # Take the nums2 from arr1, and sort in desc order so we can take down to a certain y.
        arr2 = [(arr1[i][1], i) for i in range(N)]
        arr2.sort(reverse=True)
        # sort queries in order of y.
        queries = [(queries[i][0], queries[i][1], i) for i in range(M)]
        queries.sort(key=lambda q: q[1], reverse=True)
        # Seg tree for range maximum.
        root = Node(0, N - 1)
        # answer for each queries
        ans = [0] * M
        i = j = 0
        for x, y, idx in queries:
            while j < N and arr2[j][0] >= y:
                # activate these indexes
                i = arr2[j][1]
                root.update(i, arr1[i][0] + arr1[i][1])
                j += 1
            # find from arr1 which indexes onwards we can consider for range maximum based on x.
            i = bisect_left(arr1, x, key=lambda a: a[0])
            ans[idx] = root.find(i, N - 1)
        return ans