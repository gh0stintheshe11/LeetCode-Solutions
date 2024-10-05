# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict

        def dfs(node, curr_sum):
            nonlocal count
            if not node:
                return

            curr_sum += node.val

            if curr_sum == targetSum:
                count += 1

            count += prefix_sums[curr_sum - targetSum]

            prefix_sums[curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            prefix_sums[curr_sum] -= 1

        count = 0
        prefix_sums = defaultdict(int)
        dfs(root, 0)
        return count