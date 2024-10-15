class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        from typing import List
        
        # Using a lazy segment tree to handle range flip and sum efficiently
        class SegmentTree:
            def __init__(self, nums: List[int]):
                self.n = len(nums)
                self.tree = [0] * (4 * self.n)
                self.lazy = [0] * (4 * self.n)
                self._build(nums, 0, 0, self.n - 1)
            
            def _build(self, nums: List[int], node: int, start: int, end: int):
                if start == end:
                    self.tree[node] = nums[start]
                else:
                    mid = (start + end) // 2
                    left_child = 2 * node + 1
                    right_child = 2 * node + 2
                    self._build(nums, left_child, start, mid)
                    self._build(nums, right_child, mid + 1, end)
                    self.tree[node] = self.tree[left_child] + self.tree[right_child]
            
            def _update_range(self, node: int, start: int, end: int, l: int, r: int):
                if self.lazy[node]:
                    self.tree[node] = (end - start + 1) - self.tree[node]
                    if start != end:
                        left_child = 2 * node + 1
                        right_child = 2 * node + 2
                        self.lazy[left_child] ^= 1
                        self.lazy[right_child] ^= 1
                    self.lazy[node] = 0
                
                if start > end or start > r or end < l:
                    return
                
                if start >= l and end <= r:
                    self.tree[node] = (end - start + 1) - self.tree[node]
                    if start != end:
                        left_child = 2 * node + 1
                        right_child = 2 * node + 2
                        self.lazy[left_child] ^= 1
                        self.lazy[right_child] ^= 1
                    return
                
                mid = (start + end) // 2
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self._update_range(left_child, start, mid, l, r)
                self._update_range(right_child, mid + 1, end, l, r)
                self.tree[node] = self.tree[left_child] + self.tree[right_child]
            
            def _query_sum(self, node: int, start: int, end: int, l: int, r: int) -> int:
                if start > end or start > r or end < l:
                    return 0
                
                if self.lazy[node]:
                    self.tree[node] = (end - start + 1) - self.tree[node]
                    if start != end:
                        left_child = 2 * node + 1
                        right_child = 2 * node + 2
                        self.lazy[left_child] ^= 1
                        self.lazy[right_child] ^= 1
                    self.lazy[node] = 0
                
                if start >= l and end <= r:
                    return self.tree[node]
                
                mid = (start + end) // 2
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                left_sum = self._query_sum(left_child, start, mid, l, r)
                right_sum = self._query_sum(right_child, mid + 1, end, l, r)
                return left_sum + right_sum
            
            def flip(self, l: int, r: int):
                self._update_range(0, 0, self.n - 1, l, r)
            
            def sum(self, l: int, r: int) -> int:
                return self._query_sum(0, 0, self.n - 1, l, r)
        
        result = []
        n = len(nums1)
        seg_tree = SegmentTree(nums1)
        sum_nums2 = sum(nums2)
        
        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                seg_tree.flip(l, r)
            elif query[0] == 2:
                p = query[1]
                total_flipped_1s = seg_tree.sum(0, n - 1)
                sum_nums2 += total_flipped_1s * p
            elif query[0] == 3:
                result.append(sum_nums2)
        
        return result