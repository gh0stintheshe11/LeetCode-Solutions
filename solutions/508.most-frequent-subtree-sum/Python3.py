# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from typing import Optional, List

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            count[subtree_sum] += 1
            return subtree_sum
        
        count = defaultdict(int)
        dfs(root)
        
        max_frequency = max(count.values())
        return [s for s, freq in count.items() if freq == max_frequency]