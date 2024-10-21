from typing import List

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)
    
    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])
    
    def query(self, left, right):
        result = 0
        left += self.size
        right += self.size
        while left < right:
            if left & 1:
                result = max(result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = max(result, self.tree[right])
            left //= 2
            right //= 2
        return result

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        segment_tree = SegmentTree(max_val + 1)
        
        max_length = 0
        for num in nums:
            max_prev_length = segment_tree.query(max(0, num - k), num)
            current_length = max_prev_length + 1
            segment_tree.update(num, current_length)
            max_length = max(max_length, current_length)
        
        return max_length