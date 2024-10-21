# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
import heapq
from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        queue = deque([root])
        level_sums = []

        while queue:
            level_length = len(queue)
            level_sum = 0

            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)

        if len(level_sums) < k:
            return -1

        # Find the kth largest element using a min-heap
        heapq.heapify(level_sums)
        return heapq.nlargest(k, level_sums)[-1]